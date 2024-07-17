# Discord Bot: Basics

## Process of Creating a Discord Bot

### 1. Creating the Application

1. Go to https://www.discord.com/developers/applications
2. Click on `New Application`
3. Fill in the name and validate
4. in the sidebar, click on `Bot`
5. Generate a token and copy it somewere (<span style="color:red">Private</span>)
6. Under `Privileged Gateway Intents`, activate the three switches

### 2. Inviting the bot

1. Get the Application ID, under `General Information` in the sidebar
2. Get the Bot Permissions Number, under `bot` in the sidebar
3. Build the invite url from the template: https://discord.com/oauth2/authorize?client_id=[APPLICATION_ID]&permissions=[BOT_PERMISSION_NUMBER]&scope=bot%20applications.commands
4. Open the invite in a browser (<span style="color:red">You must have a server you are authorized to add bot to</span>)

### 4. Coding

1. Install the package `pip install discord`
2. have this minimal code:
    ```py
    import discord
    from discord.ext import commands

    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    bot.run('BOT_TOKEN')

    ```

---

## Then...

- To send a message from the bot (in the context): `await ctx.send(str(result))`

- To create an event listener:
    ```py
    @bot.event
    async def on_ready():
        """called when the bot is ready!"""
        print('bot ready!')

    ```

- To create a command handler:
    ```py
    @bot.command()
    async def command_naem(ctx: commands.Context):
        ctx.send("A message to send in the server!")
    ```
    The decorator `@bot.command()` can take optional:
    - `name`: the name of the command in Discord.
    - `aliases`: the aliases (other names) of the command
    The function can take the command arguments
