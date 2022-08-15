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
bot = commands.Bot(command_prefix="t!", intents=discord.Intents.all())
account = MyPlexAccount(config['plex_user'], config['plex_pass'])
plex = account.resources()[0].connect()  # returns a PlexServer instance
admin_channel = None


print("Connected to Plex API")


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
            await after.send(f"You already have an active trial. Your trial ends on {trial_end.strftime('%m-%d-%Y %l:%M %p')}")
            return
        # deny access
        await after.send(config['deny_message'])
        await admin_channel.send(f"{after.mention} tried to receive another trial and was denied.")
        return
    # give access - send dm asking for email
    msg = await after.send("Please reply with your **Plex Email Address**, then your invite will be sent!")
    def check(m):
        if m.author.id != after.id or m.channel != msg.channel: return
        # check if email is valid
        if not re.match(r"[^@]+@[^@]+\.[^@]+", m.content):
            asyncio.run(after.send("Please reply with a valid Plex email address."))
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
    await admin_channel.send(f"{after.mention} has been invited to the trial server.\n Trial End: {trial_end}")


@bot.command()
async def trialdb(ctx):
    users = db.get_all_users()
    title1 = "ACTIVE TRIALS"
    title2 = "ENDED TRIALS"
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
    embed1 = discord.Embed(title=title1, description=desc1, color=0x7575fc)
    embed2 = discord.Embed(title=title2, description=desc2, color=0x7575fc)
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
        trial_end = datetime.datetime.strptime (trial_end,'%Y-%m-%d %H:%M:%S')
        if ended == False and trial_end < datetime.datetime.now():
            member = bot.get_guild(config['guild_id']).get_member(id)
            remove_invite(email)
            db.update_user(id, name, email, trial_end, True)
            try:
                await bot.get_user(id).send(config['end_message'])
                await admin_channel.send(f"{bot.get_user(id).mention}'s trial has ended.")
            except: pass


update_users.start()
bot.run(config['token'])
