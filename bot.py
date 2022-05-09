import re
import json
import asyncio
import discord
import datetime
import nest_asyncio
from discord.ext import tasks, commands
from plexapi.myplex import MyPlexAccount

from plexapi.exceptions import BadRequest

from db import DB

nest_asyncio.apply()
config = json.load(open('config.json'))
db = DB('users.db')

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())
account = MyPlexAccount(config['plex_user'], config['plex_pass'])
plex = account.resources()[0].connect()  # returns a PlexServer instance

print("Connected to Plex API")

admin_channel = None

def remove_invite(email):
    try: account.removeFriend(email)
    except: 
        try: account.cancelInvite(email)
        except: pass

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    global admin_channel
    admin_channel = bot.get_channel(config['admin_channel_id'])

@bot.event
async def on_member_update(before, after):
    if before.roles == after.roles:
        return
    role = discord.utils.get(after.roles, name=config['role_name'])
    if role is None: return
    
    if db.get_user(after.id) is not None:
        id, name, email, trial_end, ended = db.get_user(after.id)
        # trial_end is in the format '%Y-%m-%d %H:%M:%S'
        trial_end = datetime.datetime.strptime(trial_end, '%Y-%m-%d %H:%M:%S')
        if not ended:
            await after.send(f"You have already been invited. Your trial period ends on {trial_end.strftime('%d %b %Y')}")
            return
        
        # deny access
        cooldown = trial_end + datetime.timedelta(hours=config['cooldown_period'])
        await after.remove_roles(role)
        await after.send(config['deny_message'] + f"\nTry again after {cooldown.strftime('%d %b %Y')}")
        await admin_channel.send(f"{after.mention} tried to join but was denied access.\nOn cooldown until {cooldown.strftime('%d %b %Y')}")
        return
    
    # give access
    # send dm asking for email
    msg = await after.send("Please enter your Plex email address so we can invite you to our Plex-Share")
    
    def check(m):
        if m.author.id != after.id or m.channel != msg.channel: return
        # check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", m.content):
            asyncio.run(after.send("Please enter a valid email address"))
            return False
        return True
    msg = await bot.wait_for('message', check=check)
    
    try: account.inviteFriend(msg.content, plex)
    except BadRequest:
        remove_invite(msg.content)
        try:
            account.inviteFriend(msg.content, plex)
        except:
            await after.send("Something went wrong. Please try again later.")
        
        
    trial_end = datetime.datetime.now() + datetime.timedelta(hours=config['trial_period'])
    trial_end = trial_end.strftime('%Y-%m-%d %H:%M:%S')
    db.insert(after.id, after.name, msg.content, trial_end)
    await after.send(config["success_message"])
    await admin_channel.send(f"{after.mention} has been invited to the Trial Plex-Share.\nTrial period ends on {trial_end}")

@bot.command()
async def trialdb(ctx):
    users = db.get_all_users()
    title1 = "Users list"
    title2 = "Cooldown list"
    
    desc1 = "```"
    desc2 = "```"
    for (i, user) in enumerate(users):
        id, name, email, trial_end, ended = user
        if ended:
            desc2 += f"{i+1}. {name} - {email}\n"
        else:
            desc1 += f"{i+1}. {name} - {email}\n"
            
    desc1 += "```"
    desc2 += "```"
    
    embed1 = discord.Embed(title=title1, description=desc1, color=0x00ff00)
    embed2 = discord.Embed(title=title2, description=desc2, color=0x00ff00)
    
    await ctx.send(embed=embed1)
    await ctx.send(embed=embed2)

@tasks.loop(minutes=15)
async def update_users():
    await bot.wait_until_ready()
    while admin_channel is None:
        await asyncio.sleep(1)
    users = db.get_all_users()
    
    for user in users:
        id, name, email, trial_end, ended = user
        # trial_end is in the format '%Y-%m-%d %H:%M:%S'
        trial_end = datetime.datetime.strptime(trial_end, '%Y-%m-%d %H:%M:%S')
        if ended == False and trial_end < datetime.datetime.now():
            member = bot.get_guild(config['guild_id']).get_member(id)
            remove_invite(email)
            db.update_user(id, name, email, trial_end, True)
            try:
                await bot.get_user(id).send(config['end_message'])
                await admin_channel.send(f"{bot.get_user(id).mention}'s trial period has ended")
                await member.remove_roles(discord.utils.get(member.roles, name=config['role_name']))
            except: pass
            
        cooldown = trial_end + datetime.timedelta(hours=config['cooldown_period'])
        if cooldown < datetime.datetime.now():
            await admin_channel.send(f"{bot.get_user(id).mention}'s cooldown period is over. He can now start a new trial again")
            db.remove_user(id)

update_users.start()
bot.run(config['token'])