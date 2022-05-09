# DISCORD PLEX TRIAL BOT
A Discord bot for sending Plex invites and removing users from the server after the trial period.
<br />
<br />
# HOW IT WORKS
The bot will DM any user who has a specfic role asking the user to reply with their Plex email address. When a user replies with their email address the bot will automtically send the user an invite to your Plex server. Once the trial period has ended the bot will automatically remove the user from the Plex server. All trials begin from the time the invite was sent.

*Reaction Roles are a great way to fully automate your trials, otherwise if you want to have more control you can always manually add the role to the user.*
<br />
<br />
### COOLDOWN
There is a cooldown period that you can set, which will allow users to only request a trial after the time period has elapsed. This is great to stop abuse.
<br />
<br />
### LOGGING
You can set the bot to log all actions to a specified channle of your choice
<br />
<br />
### DATABASE
There is a sqlite database file so you can view and make modifications. This is helpful in case a user replies with an incorrect email address. Simply remove the users entry from the database, then the user can make a new request for a trial. 
<br />
<br />
### MESSAGES
You can set custom messages that the bot will DM user with. 
- When a user is denied from trying to request another trial before their cooldown period has ended.
- When an invite has successfully been sent after replyig with a confirmed Plex email address.
- When the users trial has ended.
<br />

# SETUP

## <ins>STEP 1</ins>

Download this repository [HERE](https://github.com/zluckytraveler/discord-hierarchy-roles/archive/refs/heads/main.zip) 
<br />
<br />
## <ins>STEP 2</ins>
Learn how to create a <ins>Discord Bot</ins> and find a <ins>Discord ID</ins>.<br />
If you already know how to do this continue to STEP 3.

### DISCORD BOT
1. Go to [Discord Developer](https://discord.com/developers)
2. Create a Application.
3. Create a Bot.
4. Enable intents for the folowing settings: **PRESENCE INTENT, SERVER MEMBERS INTENT, MESSAGE CONTENT INTENT**
5. Create a token for the first time by selecting "Reset Token". Copy the token and save it, you will need it later on.
6. Select **URL Generator** located under **OAuth2**, then enable **bot** under Scopes, followed by **Administator** for Permissions.
7. Copy the generated url at he bottom of the page, and paste it into your browsers address bar.
8. Follow the Discord popup steps for inviting the bot to your Discord server.

### DISCORD ID
1. Login to your Discord Account.
2. Select the gear icon to open your user settings.
3. Select the Advance tab on the side bar.
4. Enable developer mode.
5. Right click on your Guild or Channel.
8. Now copy the ID.  
<br />

## <ins>STEP 3</ins>
Add your Bot Token, Plex credentials, Discord ID's, and configure your settings in `config.json`, and save the file.

The Discord role is the role which a user must have in order for the bot to DM the user asking for them to reply with their Plex email address.
<br />
<br />
<br />
# INSTALL

## LOCAL

### <ins>STEP 1</ins>

Change the directory to where the files are stored.

```cd <PATH TO DIRECTORY>```

### <ins>STEP 2</ins>

Install the requirements. <br />

```pip3 install -r requirements.txt```


### <ins>STEP 3</ins>

Run the Bot. <br />

```python3 bot.py```
