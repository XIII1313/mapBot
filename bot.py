import discord
from discord.ext import commands
import random


Client = discord.Client() #Initialise Client
client = commands.Bot(command_prefix = "!") #Initialise client bot
replyList = ["Erangel", "Miramar"]


def chooseRandomObjectFromList(list):
    index = random.randint(0, len(list) - 1)
    randomObject = list[index]
    return randomObject


print("starting...")


@client.event
async def on_ready():
    print("Bot is online and connected to Discord")


@client.event
async def on_message(message):
    print("recieved message")
    if message.content == "map":
        mapName = chooseRandomObjectFromList(replyList)
        await client.send_message(message.channel, mapName)


client.run("NDM2NTU5MDQwMDcyNTE1NTg0.DbpUrA.Ka1eRWTagJtIMjD6NY2GQ6pgKK8")
