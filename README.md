# NetherGames Discord Bot

Rewritten by [@plun1331](https://plun1331.github.io)

## Commands

### Public Commands

These commands can be used by any user.

`ng!help` - Displays a list of commands.

`ng!ping` - Check the bot's latency.

`ng!leaderboard <leaderboard> [game]` - Displays the current top players on a specific leaderboard.

`ng!player <player>` - Displays a player's statistics.

### Restricted Commands

These commands are restricted to the bot's owner, in other words, whoever has administrative access to the application in the Discord Developer Portal.

`ng!load <extension>` - Load a discord.py extension.

`ng!unload <extension>` - Unload a discord.py extension.

`ng!reload <extension>` - Reload a discord.pt extension.

`ng!stop` - Logs the bot out of the bot account, thus shutting down the bot.

## Requirements

discord.py - `pip install discord.py`

tabulate - `pip install tabulate`

## Start the Bot

To start the bot, put your Discord Bot token in `config.ini` and execute `main.py`.
