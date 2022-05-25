# DISCORD PLEX TRIAL BOT
A Discord bot for sending Plex invites and removing users from the Plex server after a trial period has ended.
<br />
<br />
# HOW IT WORKS
The bot will DM any user who has a specfic role asking the user to reply with their Plex email address. When a user replies with their email address the bot will automtically send the user an invite to your Plex server. Once the trial period has ended the bot will automatically remove the user from the Plex server. All trials begin from the time the invite was sent.

*Reaction Roles are a great way to fully automate your trials, otherwise if you want to have more control over your invites, you can manually add the role to the user.*
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
There is a sqlite database file that will be automat8ically made upon the first trial invite. You can view and make modifications to the file, in case a user replies with an incorrect email address. Simply remove the entry from the database, then the user can make a new request for a trial. 
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
| `cooldown_period` | Integer | An integer value for the length of time in hours |
| `trial_period` |  Integer | An integer value for the length of time in hours |
| `deny_message` | String | The messages sent when a user requests a trial before their cooldown period has ended |
| `success_message` | String | The messages sent when a Plex invite has successfully been sent |
| `end_message` | String | The messages sent when a users trial has ended |
<br />

# INSTALL

## DOCKER CLI

Simply run the command.

```docker run --name Plex-Trial --restart=unless-stopped -d -v /PATH TO CONFIG/config.json:/bot/config.json -v /PATH TO DATABASE/users.db:/bot/users.db -d zluckytraveler/discord-plex-trial ```
<br />
<br />
## DOCKER BUILD

### <ins>STEP 1</ins>
Change the directory to where the files are stored.

```cd <PATH TO DIRECTORY>```

### <ins>STEP 2</ins>
Build the image. The image name must be all lowercase without any spacing

```docker build -t <YOUR IMAGE NAME> .```

### <ins>STEP 3</ins>
Start the container by using the Docker run command.

```docker run -d --restart=unless-stopped <YOUR IMAGE NAME>```
<br />
<br />
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
