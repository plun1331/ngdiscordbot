import discord
from discord.ext import commands
import aiohttp
import json


class Player(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['profile', 'player'])
    async def p(self, ctx, input=""):
        if input:
            player = input.replace(" ", "%20")
            print(str(player))
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get('https://api.nethergames.org/?action=stats&player=' + str(player)) as resp:
                        data = await resp.json()
                except aiohttp.ClientError:
                    async with session.get('https://apiv2.nethergames.org/?action=stats&player' + str(player)) as resp:
                        data = await resp.json()
                except BaseException as e:
                    await ctx.send("Sorry, that player could not be found. Perhaps you made a typo?")
                    data = await resp.json()
            if not data:
                await ctx.send("Sorry, that player could not be found. Perhaps you made a typo?")
            else:
                embed = discord.Embed(title="Player statistics for " + str(data["name"]),
                                      url="https://account.nethergames.org/player/" + str(player))
                embed.set_author(name="NetherGames Network", url="https://nethergames.org",
                                 icon_url="https://cdn.nethergames.org/img/logo_small_trans.png")
                embed.set_thumbnail(url="https://player.nethergames.org/avatar/" + str(player))
                embed.add_field(name="Kills", value=str(data["kills"]), inline=True)
                embed.add_field(name="Deaths", value=str(data["deaths"]), inline=True)
                embed.add_field(name="K/DR", value=str(round(int(data["kills"]) / int(data["deaths"]), 2)), inline=True)
                embed.add_field(name="Wins", value=str(data["wins"]), inline=True)
                embed.add_field(name="Level", value=str(data["level"]), inline=True)
                embed.add_field(name="Credits", value=str(data["statusCredits"]), inline=True)
                if not data["ranks"]:
                    data["ranks"] = "Guest"
                embed.add_field(name="Rank", value=str(data["ranks"]), inline=True)
                if not data["tier"]:
                    data["tier"] = "No tier"
                embed.add_field(name="Tier", value=str(data["tier"]), inline=True)
                embed.add_field(name="First seen", value=str(data["firstJoin"]), inline=True)
                embed.add_field(name="Last seen", value=str(data["lastJoin"]), inline=True)
                if int(data["online"]) == 1:
                    embed.set_footer(text="Online - playing on " + str(data["lastServer"]),
                                     icon_url="https://cdn.nethergames.org/img/green.png")
                else:
                    embed.set_footer(text="Offline - last seen on " + str(data["lastServer"]),
                                     icon_url="https://cdn.nethergames.org/img/red.png")
                try:
                    await ctx.send(embed=embed)
                except BaseException as e:
                    await ctx.send("Backtrace: " + str(e))
        else:
            await ctx.send("Usage: ng!p <player>")


def setup(bot):
    bot.add_cog(Player(bot))
