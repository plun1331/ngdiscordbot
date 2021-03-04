import discord
from discord.ext import commands

class Player(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def help(self, ctx, input = ""):
        embed = discord.Embed(title='Help', description="""`ng!help` - Displays a list of commands.
        `ng!ping` - Check the bot's latency.
        `ng!leaderboard <leaderboard> [game]` - Displays the current top players on a specific leaderboard.
        `ng!player <player>` - Displays a player's statistics.""")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Player(bot))
