import discord
from discord.ext import commands
import os
import asyncio
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running!"

def run():
    app.run(host="0.0.0.0", port=10000)

def keep_alive():
    t = Thread(target=run)
    t.start()


intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


async def main():
    await bot.load_extension("tickets")

    keep_alive()

    TOKEN = os.getenv("TOKEN")
    await bot.start(TOKEN)


asyncio.run(main())
