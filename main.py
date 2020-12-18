import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix = "?") 

# Load all Cogs on init
for filename in os.listdir("./cogs"):
  if filename.endswith(".py"):
    # Cut off .py
    client.load_extension(f"cogs.{filename[:-3]}")

# Allgemeiner Error Handler
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    ctx.send("Der angegebene Befehl wurde nicht gefunden!")

client.run(os.getenv("DISCORD_TOKEN"))