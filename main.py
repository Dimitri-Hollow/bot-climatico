import discord
from discord.ext import commands
import requests  
import asyncio

intents = discord.Intents.default()
intents.message_content = True  # Para ler mensagens
bot = commands.Bot(command_prefix="mc!", intents=intents)

bot.run("token")
