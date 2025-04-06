from discord import app_commands
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Test of de bot werkt")
    async def ping(self, interaction):
        await interaction.response.send_message("Pong! De bot leeft.")

async def setup(bot):
    await bot.add_cog(Ping(bot))
