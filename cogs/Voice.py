import discord
from discord.ext import commands
from discord.utils import get

class Voice(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command()
  async def join(self, ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(self.client.voice_client, guild=ctx.guild)

    if voice and voice.is_connected():
      await voice.move_to(channel)
    else:
      voice = await channel.connect()

  @commands.command()
  async def leave(self, ctx):
    await ctx.voice_client.disconnect()

def setup(client):
  client.add_cog(Voice(client))