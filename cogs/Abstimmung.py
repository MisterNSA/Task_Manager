import discord
from discord.ext import commands

class Abstimmung(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["vote","Vote","voting","Voting"])
  async def Abstimmung(self, ctx, *, question):
    """- Erstellt eine Abstimmung | Syntax: '?vote {Frage}'"""
    pass
  #?Vote {Frage}
  #-Datenbankeintrag erstellen 
  #ID / Frage / Up_Vote / Down_Vote/ Already_Voted
  #-Frage ausgeben, ID ausgeben / Beide Vote Befehle ausgeben
    
  @commands.command(aliases=["ja","Ja","Up","up"])
  async def Up_Vote(self, ctx, Id):
    """- Trägt einen Upvote in die Umfrage ein | Syntax: ja{Id}"""
    pass
  #Syntax: ?Ja {ID}
  #- If User not in Already_Voted
  #Else: print("Du hast schon gevoted")
  #- UP_Vote += 1
  #- Add User to Already_Voted
    
    
  @commands.command(aliases=["Nein","nein","No","no"])
  async def Down_Vote(self, ctx, Id):
    """- Trägt einen Downvote in die Umfrage ein | Syntax ?nein {id}"""
    pass
  #Syntax: ?Nein {ID}
  #- If User not in Already_Voted
  #Else: print("Du hast schon gevoted")
  #- Down_Vote += 1
  #- Add User to Already_Voted


  @commands.command(aliases=["Ergebnis","ergebnis","Result","result"])
  async def Get_Result(self, ctx, Id):
    """- Gibt das Ergebnis der Abstimmung aus"""
    pass
  
  #Syntax ?Result {ID}
  #- Frage ausgeben, Upvotes ausgeben, Downvotes ausgeben
  #- Spalte in DB löschen
 
 
  @Abstimmung.error
  async def Abstimmung_Error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Bitte übergib alle benötigten Parameter.\n ?vote {Frage}")



def setup(client):
  client.add_cog(Abstimmung(client))