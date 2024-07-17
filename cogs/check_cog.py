from datetime import datetime

import discord
from discord import app_commands
from discord.ext import commands

from utils import dprint


class CheckCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        dprint("loaded successfully!", src=self.__cog_name__)

    @commands.command()
    async def whoami(self, ctx: commands.Context):
        dprint(f"{ctx.author.display_name} called {
               ctx.command.name}!", src=self.__cog_name__)

        embed = discord.Embed(color=ctx.author.color,
                              title=ctx.author.display_name,
                              description=ctx.author.id)

        embed.set_thumbnail(url=ctx.author.avatar)
        embed.add_field(name="Created at",
                        value=ctx.author.created_at, inline=False)

        maxlen = max([len(f[0]) for f in ctx.author.flags])

        for flag in ctx.author.flags:
            embed.add_field(name=flag[0].ljust(
                maxlen), value=flag[1], inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx: commands.Context):
        dprint(f"{ctx.author.display_name} called {
               ctx.command.name}!", src=self.__cog_name__)

        ping_embed = discord.Embed(color=discord.Color.red(),
                                   title="Ping", description="Latency in ms")
        ping_embed.add_field(name=f"{self.bot.user.name}'s Latency", value=f"{
            round(self.bot.latency * 1000, 2)}ms", inline=False)
        ping_embed.set_thumbnail(url=self.bot.user.display_avatar)
        ping_embed.set_footer(text=f"requested by {
            ctx.author.display_name}", icon_url=ctx.author.display_avatar)

        await ctx.send(embed=ping_embed)

    @app_commands.command(description='Gives the current datetime')
    async def now(self, inter: discord.Interaction):
        dprint(f"{inter.user.display_name} called {
               inter.command.name}!", src=self.__cog_name__)

        dt = datetime.now()
        await inter.response.send_message(str(dt), ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(CheckCog(bot))
