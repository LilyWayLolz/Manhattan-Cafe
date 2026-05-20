import discord
from discord import File
from discord import default_permissions
import random
import json
import datetime
import lxml
from bs4 import BeautifulSoup

with open("config.json", "r") as f:
    config = json.load(f)
    
with open("cafes.json", "r") as f:
    replies = json.load(f)

TOKEN = config["token"]
REPLIES = replies

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.moderation = True

bot = discord.Bot(command_prefix="-", intents=intents)
testingservers = [1281122097778921515, 713322963193167913, 1345800065800736768]

@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.streaming, name="Coffee Island"
        )
    )
    print("We Are Ready Now")


bot.run(TOKEN)
