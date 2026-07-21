import discord
from discord.ext import commands
import os
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

@bot.event
async def on_ready():
    await bot.load_extension("tickets")
    print(f"تم تشغيل البوت: {bot.user}")


keep_alive()

TOKEN = os.getenv("TOKEN")

bot.run(TOKEN)
