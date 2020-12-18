import discord
from discord.ext import commands

class loader(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def load(self, ctx, extension):
    """- Loads cogs | syntax 'load {cog}'"""
    self.client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} was loaded")

  @commands.command()
  async def unload(self, ctx, extension):
    """- Unloads cogs | syntax 'unload {cog}'"""
    self.client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} was unloaded")

  @commands.command()
  async def reload(self, ctx, extension):
    """- Reloads cogs | syntax 'reload {cog}'"""
    self.client.unload_extension(f"cogs.{extension}")
    self.client.load_extension(f"cogs.{extension}")
    await ctx.send(f"{extension} was reloaded")

def setup(client):
  client.add_cog(loader(client))