
import discord
from discord.ext import commands
import random

class Rolle(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=["role","Role","rolle"])
  async def Rolle(self, ctx):
    """- Gibt dir eine zufällige Geheime Rolle: '?rolle'"""
  

    Rollen = {1: "Speedrunner",
                2: "Detektiv",
                3: "Impostor",
                4: "SuS",
                5: "Lügner",
                6: "Camgirl",
                7: "Admin",
                8: "Der Mann mit der Hose",
                9: "Vent Schrubber",
                10: "Troll",
                11: "Master of Bullshit",
                12: "Spontaner Schlaganfall",
                13: "Stalker",
                14: "Baumkuschler",
                15: "Rage-Kiddie",
                16: "Saboteur",
                17: "Necrophil",
                18: "Tänzer",
                19: "Das Sprachtalent",
                20: "Drückeberger",
                21: "Autist",
                22: "Rapper",
                23: "Prospagnos",
                24: "Marathonläufer",
                25: "Rätselhaft",
                26: "Orientierungslos",
                27: "Agorabhob",
                28: "Sänger",
                29: "Reporter",
                30: "Hartz VI Empfänger"}

    Rollen_Beschreibung = {1: " - To fast 4 you, speedrunne deine Tasks oder kills!",
                           2: " - Somethings fishy, Nutze deine Detektivskills um herauszufinden was!",
                           3: " - Willkommen auf der dunklen Seite. Hilf dem Impostor zu gewinnen",
                           4: " - Spiele als wärst du Impostor. Ein sehr schlechter Impostor. Also MisterNSA",
                           5: " - Lüge wie niemand zuvor gelogen hat... Außer Personen mit dieser Rolle",
                           6: " - Halte Abstand und stalke alle über die Cams oder Türsensoren. Wenn du Zeit hast, geht natürlich auch ein Stream auf CornHub!",
                           7: " - Ich hasse meinen Job! Campe am Admin-Table. Tipp falls es nicht funktioniert: Hast du das Gerät schonmal ein und wieder ausgeschaltet",
                           8: " - Du liebst Hosen, deshalb muss jeder andere sie auch anhaben. Also ziehe anderen deine Hose an, oder ziehe dir ihre an!",
                           9: " - Vents müssen glänzen, deshalb verbringst du zum reinigen 10 Sekunden auf jedem Vent, an dem du vorbei kommst. Als impostor musst du mindestens 1 Ventkill machen",
                           10: " - Verarsche einfach alle nach Strich und Faden. Vorallem Phoenix",
                           11: " - Es ist dir überlassen, was für einen Bullshit du fabrizierst.",
                           12: " - Spiele so dumm, wie du nur kannst. Du verstehst weder die Argumente anderer, noch ergeben deine irgendeinen Sinn",
                           13: " - Suche dir nach jedem Meeting eine Person aus und folge ihr 20 Sekunden. Die 20 Sekunden liegen in deinem Ermessen",
                           14: " - Sobald du eine Pflanze siehst, musst du sie umarmen. Gilt nicht für Gewächshäuser, das wäre sexuelle Belästigung",
                           15: " - Suche dir am Anfang der Runde jemanden aus und schiebe krankhaft alle Schuld auf ihn oder sie",
                           16: " - Als impostor musst du immer sabotieren, sobald der cooldown abgelaufen ist. Als Crewmate musst du von Sabotagen weglaufen, anstatt sie zu fixen",
                           17: " - Wenn du eine Leiche findest, stehe so lange in ihr, bis jemand anderes sie reportet. Verstecke sie, sonst locht jemand anderes ein. Als Impostor ist dies nur mindestens einmal zu machen",
                           18: " - Wenn du jemanden siehst, musst du ihn oder sie kurz antanzen",
                           19: " - Muss die ganze Runde in bescheuerten Dialekten reden. Dänglisch geht auch",
                           20: " - Du darfst keine Leichen reporten sondern musst alles über Emergency Meetings klären.",
                           21: " - Spreche nicht mehr als 10 Wörter pro Meeting",
                           22: " - Alles was du sagst sind Reime und normale Sätze keine",
                           23: " - Du kannst dir weder Namen noch Farben merken, dafür bleiben dir äußere Merkmale besonders gut im Kopf. Benne Leute nur anhand ihrer Accesories",
                           24: " - Gehe nach jeder Task zur am weitesten entfernten Task und mache diese als nächstes. Zumindest bis zum ersten Meeting",
                           25: " - Deine geistig moralischen Mechanismen sind mysteriös und komplex. Deshalb sprichst du nur in Rätseln und umschreibst anstatt namen, Farben oder Orte zu nennen",
                           26: " - Du kannst keine Ortsangaben nutzen sondern Räume nur anhand ihrer Einrichtung beschreiben, wodurch Flure leider entfallen. Außerdem erinnerst du dich nur an die 3 letzten Räume, in denen du warst",
                           27: " - Du hast Angst vor der Außenwelt und offenen Plätzen. Suche dir zu Beginn des Spiels einen Raum und begib dich alle 3 Tasks dort hin. Um dich zu erholen bleibst du kurz dort.",
                           28: " - Du musst alle deine Argumente zur Melodie eines beliebigen Liedes vortragen. Präferiert Dubstep oder Hardbass",
                           29: " - Du musst Krankhaft alles ungemuted kommentieren, was du machst. Ich hasse dich jetzt schon!",
                           30: " - Du lebst nach den 10 A's zum Erfolg(Alle anfallenden Arbeiten auf andere abschieben, anschließend anscheißen, aber  Anständig!) und machst deshalb keine Tasks. Dafür schießt du besonders laut auf Leute, die die Tasks nicht schnell genug machen"}

    Rolle_ID, Rolle_name = random.choice(list(Rollen.items()))
    Rolle_beschreibung = Rollen_Beschreibung[Rolle_ID]
    response = "----------\n" + Rolle_name + Rolle_beschreibung
    await ctx.author.send(response)

    @Abstimmung.error
    async def Abstimmung_Error(self, ctx, error):
      await ctx.send("Syntax: ?rolle")

def setup(client):
  client.add_cog(Rolle(client))
