import discord
from discord.ext import commands, tasks
from discord.ext.commands import MissingPermissions
import json
import os 
import asyncio
import datetime
from random import choice
import random 
from asyncio import sleep 
from discord import Embed, Color
from discord import Member, DMChannel, Embed, NotFound

if os.path.exists(os.getcwd() + "/config.json"):
    with open("./config.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"Token": "" , "Prefix": "$"}

    with open(os.getcwd() + "/config.json", "w+") as f:
        json.dump(configTemplate, f)

token = configData["Token"]
Prefix = ["!" ]
intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix=("!"), intents=intents)

@bot.event
async def on_ready():
    print("im ready")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='RX VIDEOS'))


@bot.command()
async def youtube(ctx):
    await ctx.send("This is the RX channel: https://www.youtube.com/c/RrrrrrrXXX")

@bot.command()
async def instagram(ctx):
    await ctx.send("This is the RX instagram: https://www.instagram.com/rrrrrrrxxx/")

@bot.command()
async def facebook(ctx):
    await ctx.send("This is the RX facebook: https://www.facebook.com/rrrrrrrxxx ")


videos = ["https://youtu.be/tQMBkWg9lT0" , "https://youtu.be/AzexY8j70SE", "https://youtu.be/4K-XfEM_q3I","https://youtu.be/Ad9gLdgCnXE","https://www.youtube.com/watch?v=IF4ysmzhzDY&t=96s","https://www.youtube.com/watch?v=IqHf0PyXHD0&t=313s","https://www.youtube.com/watch?v=UanNY_631Ts&t=592s"  ] 

@bot.command()
async def rxvideo(ctx):
    await ctx.send("I found a good video")
    await ctx.send(choice(videos))

@bot.command(pass_context=True)
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@bot.command(pass_context=True)
async def dc(ctx):
    server = ctx.message.guild.voice_client
    await server.disconnect()


bot.run(token)