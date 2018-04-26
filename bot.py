import discord
from discord.ext import commands
import random


Client = discord.Client() #Initialise Client
client = commands.Bot(command_prefix = "!") #Initialise client bot
replyList = ["Erangel", "Miramar"]
replyListHey = ["hi!", "hey!", "hello!"]

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
    if message.content.lower() == "map":
        mapName = chooseRandomObjectFromList(replyList)
        await client.send_message(message.channel, mapName)
        
    elif message.content.lower() in ["hey", "hello", "hi"]:
        reply = chooseRandomObjectFromList(replyListHey)
        await client.send_message(message.channel, reply)
        
    elif message.content.lower() in ["good bot", "good bot!"]:
        reply = "Thanks"
        await client.send_message(message.channel, reply)


client.run("NDM2NTU5MDQwMDcyNTE1NTg0.DbpUrA.Ka1eRWTagJtIMjD6NY2GQ6pgKK8")
