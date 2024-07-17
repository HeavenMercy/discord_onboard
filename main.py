import asyncio
import os

import discord
from discord import app_commands
from discord.ext import commands, tasks

from utils import Config, dprint, get_bot_key, get_statuses

cfg = Config().load()

statuses = get_statuses()

bot_key = get_bot_key()

# ---------------------------------------------------------------------------

bot = commands.Bot(
    command_prefix=cfg.get('command_prefix'), intents=discord.Intents.all())


@tasks.loop(seconds=cfg.get('status_update_delay'))
async def change_bot_status():
    status = next(statuses)
    dprint(f"changing status to '{status}'")
    await bot.change_presence(activity=discord.Game(status))


@bot.event
async def on_ready():
    dprint('bot connected successfuly!')
    await sync_slash_commands()
    change_bot_status.start()


@bot.command(aliases=['hi', 'morning', 'hey'])
async def hello(ctx: commands.Context):
    dprint(f"[{ctx.author.display_name} called {ctx.command.name}!")

    msg = f"Hello there, {ctx.author.mention}"
    await ctx.send(msg)


@bot.tree.command(description='tells what the user said')
@app_commands.describe(
    message='the message to tell',
    tts="say it louder!")
async def tell(inter: discord.Interaction, message: str, tts: bool = False):
    dprint(f"[{inter.user.display_name} called {inter.command.name}!")

    await inter.response.send_message(
        f"{inter.user.mention} said '{message}'.", tts=tts)


# ----------------------------------------------------------------------------


async def sync_slash_commands():
    try:
        await bot.tree.sync()
        dprint("bot's slash command loaded successfully!")
    except Exception as e:
        dprint(f"failed to sync the bot's slash command! ({str(e)})")


async def load_cogs():
    cogs_d = 'cogs'
    for f in os.listdir(cogs_d):
        if f.endswith('.py'):
            cog_mod = '.'.join([cogs_d, f[:-3]])
            dprint(f"loading `{cog_mod}`...", end=' ')
            try:
                await bot.load_extension(cog_mod)
                dprint('DONE', with_src=False)
            except Exception as e:
                dprint(f'FAIL ({str(e)})', with_src=False)


async def main():
    async with bot:
        await load_cogs()
        await bot.start(bot_key)

asyncio.run(main())
