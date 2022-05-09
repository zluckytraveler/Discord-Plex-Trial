# DISCORD PLEX TRIAL BOT
A Discord bot for sending Plex invites and removing users from the server after the trial period.
<br />
<br />
# SETUP

## <ins>STEP 1</ins>

Download this repository [HERE](https://github.com/zluckytraveler/discord-hierarchy-roles/archive/refs/heads/main.zip) 
<br />
<br />
## <ins>STEP 2</ins>
Learn how to create a <ins>Discord Bot</ins> and find a <ins>Role ID</ins>.<br />
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

### DISCORD ROLE ID
1. Login to your Discord Account.
2. Select the gear icon to open your user settings.
3. Select the Advance tab on side bar.
4. Enable developer mode.
5. Go to your server and select Server Settings.
6. Select the Roles setting.
7. Select the three vertical dots next tot he role name.
8. Now copy the Role ID.  
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
