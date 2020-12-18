import discord
from discord.ext import commands

class On_Ready(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    await self.client.change_presence(status=discord.Status.idle, activity=discord.Game("Listening to ?Help"))
    print(f"Logged in as {self.client.user}")


def setup(client):
  client.add_cog(On_Ready(client))