# DISCORD PLEX TRIAL BOT
A Discord bot for sending Plex invites and removing users from the Plex server after a trial period has ended.
<br />
<br />
# HOW IT WORKS
The bot will send a DM to a user when they receive the specfied role that you set in the `config.json` file. The DM will ask the user to reply with their Plex email address. When a user replies with their email address the bot will automtically send the user an invite to the Plex server. Once the trial period has ended the bot will automatically remove the user from the Plex server. 
<br />
<br />
All trials begin from the time the invite was sent, and a user can only request one trial, if they try to request another one, they will recieve a denial message. The bot checks for trials to remove users every 15 minutes, this even includes invites that were sent and not accepted. 
<br />
<br />
If you want to change the timeframe the bot checks for removing trials, you can edit the code in `bot.py` on line 101 `minutes=15`. You can change it to any unit or amount of time you would like. **Examples:** `seconds=30` or `hours=1`
<br />
<br />
<br />
*Reaction Roles are a great way to fully automate your trials, otherwise if you want to have more control over your invites, you can manually add the role to the user.*
<br />
<br />
### LOGGING
You can set the bot to log all actions to a specified channel of your choice
<br />
<br />
### DATABASE
There is a sqlite database file that will automatically be made upon starting the bot. You can view and make modifications to the file, in case a user replies with an incorrect email address, or you want to make adjustments. Simply remove the entry from the database, then the user can make a new request for a trial. 
<br />
<br />
### MESSAGES
You can set custom messages the bot will DM users with. 
- When an invite has successfully been sent after replying with a confirmed Plex email address.
- When a user is denied from trying to request another trial.
- When the users trial has ended.
<br />

# SETUP

## <ins>STEP 1</ins>

Download this repository [HERE](https://github.com/zluckytraveler/Discord-Plex-Trial/files/9334869/Plex-Trials.zip)
<br />
<br />
## <ins>STEP 2</ins>
Learn how to create a <ins>Discord Bot</ins> and find a <ins>Discord ID</ins>.<br />

*If you already know how to do this continue to STEP 3.*

### DISCORD BOT
1. Go to [Discord Developer](https://discord.com/developers)
2. Create a Application.
3. Create a Bot.
4. Enable intents for `PRESENCE INTENT`, `SERVER MEMBERS INTENT`, `MESSAGE CONTENT INTENT`
6. Create a token by selecting `Reset Token`, then copy and save the token, you will need it later.
7. Under `OAuth2` select `URL Generator`, then enable `bot` & `Administator` under `Scopes` & `Permissions`.
8. Copy the generated url at he bottom of the page, and paste it into your browsers address bar.
9. Follow the Discord popup steps for inviting the bot to your Discord server.

### DISCORD ID
1. Login to your Discord Account.
2. Select the gear icon to open your user settings.
3. Select the Advance tab on the side bar.
4. Enable developer mode.
5. Right click on your Guild or Channel.
8. Now copy the ID.  
<br />

## <ins>STEP 3</ins>
Configure `config.json` and save the file.

| DATA | TYPE | DESCRIPTION |
| --- | --- | --- |
| `token` | String | Your custom Discord bot token |
| `plex_user` | String | Your Plex account username |
| `plex_pass` | String | Your Plex account password |
| `admin_channel_id` | Integer | The Discord channel ID of where the bot actions are logged |
| `guild_id` | Integer | Your Discord servers ID |
| `role_name` | String | The Discord role a user must have for the bot to DM a user **(Don't Add @)** |
| `trial_period` |  Integer | An integer value for the length of time in hours |
| `deny_message` | String | The messages sent when a user requests a trial before their cooldown period has ended |
| `success_message` | String | The messages sent when a Plex invite has successfully been sent |
| `end_message` | String | The messages sent when a users trial has ended |
<br />

# INSTALL

## DOCKER

Simply run the command.
```
docker run -d  -v /PATH-TO-CONFIG/config.json:/bot/config.json -v /PATH-TO-DATABASE/users.db:/bot/users.db zluckytraveler/discord-plex-trial
```

Replace `PATH-TO-CONFIG` & `PATH-TO-DATABASE` with the path to where you stored the files from STEP 1
<br />
<br />
## LOCAL

**PREREQUISITES**
- Python 3
- Pip
<br />

**STEPS**

**1.** Change the directory to where you stored the files.
```
cd <PATH-TO-DIRECTORY>
```
<br />

**2.** Install the requirements.
```
pip install -r requirements.txt
```
<br />

**3.** Run the Bot.

**Mac & Linux**
```
python3 bot.py
```
**Windows**
```
py bot.py
```