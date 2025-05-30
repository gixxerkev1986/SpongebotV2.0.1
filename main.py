import discord
from discord.ext import commands
import asyncio
import os

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = 1356894863454376105  # <- hardcoded

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot is online als {bot.user}")
    try:
        synced = await bot.tree.sync(guild=discord.Object(id=GUILD_ID))
        print(f"Slash commands gesynchroniseerd: {len(synced)}")
        for cmd in synced:
            print(f"Command: /{cmd.name}")
    except Exception as e:
        print(f"Fout bij syncen: {e}")

async def main():
    async with bot:
        await bot.load_extension("commands.ping")
        await bot.start(TOKEN)

asyncio.run(main())
