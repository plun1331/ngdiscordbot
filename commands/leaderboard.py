import discord
from discord.ext import commands
import requests
import tabulate

class LB(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['lead', 'leaderboard'])
    async def l(self, ctx, leaderboard = "", game = ""):
        if leaderboard:
            leaderboard = str(leaderboard)
            leaderboard = leaderboard.lower()
            if game:
                game = str(game)
                game = game.upper()
            print(str(leaderboard))
            try:
                if game:
                    r = requests.get("https://api.nethergames.org/?action=leaderboards&type=wins&game=" + game)
                else:
                    r = requests.get("https://api.nethergames.org/?action=leaderboards&type=" + leaderboard)
                data = r.json()
            except BaseException as e:
                await ctx.send("Sorry, that leaderboard could not be loaded.")
        
            if not data:
                await ctx.send("Sorry, that leaderboard could not be loaded.")
            else:
                table_data = []
                number = 0
                for d in data:
                    table_data.append([])
                    table_data[number].append(number + 1)
                    table_data[number].append(str(d["player"]))
                    table_data[number].append(str(d["kdr"]))
                    table_data[number].append(str(d["kills"]))
                    table_data[number].append(str(d["deaths"]))
                    table_data[number].append(str(d["wins"]))
                    table_data[number].append(str(d["level"]))
                    table_data[number].append(str(d["credits"]))
                    number += 1
                leaderboards_data = tabulate([table_data[0], table_data[1], table_data[2], table_data[3], table_data[4]], ["#", "Name", "K/DR", "Kills", "Deaths", "Wins", "Level", "Credits"], tablefmt="grid")
                leaderboards_data2 = tabulate([table_data[5], table_data[6], table_data[7], table_data[8], table_data[9]], ["#", "Name", "K/DR", "Kills", "Deaths", "Wins", "Level", "Credits"], tablefmt="grid")
                message = "```" + leaderboards_data + "```"
                message2 = "```" + leaderboards_data2 + "```"
                try:
                    await ctx.send(f"""Leaderboard for {leaderboard}
                    {message}
                    {message2}
                    Data fetched from API cache at {str(datetime.now())}""")
                except BaseException as e:
                    await ctx.send("Backtrace: " + str(e))
        else:
            await ctx.send("""```
            Usage: ng!l <kdr|kills|wins|xp|credits> [bb|bh|br|bw|mm|sc|sw]
            Game (2nd parameter) filter only works for the wins leaderboard.
            ```""")

def setup(bot):
    bot.add_cog(LB(bot))