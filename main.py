import asyncio
import discord
import os
from discord.ext import commands


TOKEN = "MTA4ODUwMTE0NTI3NTc0NDI4Nw.G_cgc3.wc0EDpwFY73xpUdwNv3KrNdZuxJZJJbUBIhqXk"
PREFIX = "-"


intents = discord.Intents.default()
intents.message_content = True
intents.typing = False
intents.presences = False
bot = commands.Bot(command_prefix=commands.when_mentioned_or(PREFIX), intents=intents, help_command=None)

async def load():
     for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")

async def main():
    await load()
    await bot.start(TOKEN)



asyncio.run(main())