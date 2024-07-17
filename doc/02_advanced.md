# Discord Bot: Advanced

## Cogs

These are like Flask blueprints, or middlewere... Simply extensions!
To have one, create file and modify this tamplate inside to fit your need:

```py
# example relpath to file: cogs/my_cog.py

import discord
from discord.ext import commands


class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        dprint(f"loaded successfully!", src=self.__cog_name__)

    @commands.command()
    async def acommand(self, ctx: commands.Context):
        pass

async def setup(bot: commands.Bot):
    await bot.add_cog(MyCog(bot))
```

To load one into your bot: `bot.load_extension('cogs.my_cog')`

---

## Tasks

A task is usually an action/process that is schedule or executed periodically. It can be created by:
```py
# a task that runs every 5 seconds.

@tasks.loop(seconds=5)
async def a_great_task():
    pass
```

This task can then be started: `a_great_task.start()`

---

## Slash Commands

- To create a slash command:

**Directly on the bot:**
```py
@bot.tree.command(description='some slash command description')
async def a_slash_command(inter: discord.Interaction):
    await inter.response.send_message(...) # to send back a message
```

**Inside a Cog**
```py
from discord import app_commands

@app_commands.command(description='some slash command description')
async def a_slash_command(inter: discord.Interaction):
    await inter.response.send_message(...) # to send back a message
```

- To sync the commands with discord servers : `bot.tree.sync()`
