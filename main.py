import discord
from discord.ext import commands
import os

intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="-",
    intents=intents
)

@bot.event
async def on_ready():
    print(f"تم تشغيل البوت: {bot.user}")

TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)
