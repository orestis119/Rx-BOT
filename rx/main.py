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
    configTemplate = {"Token": "" , "Prefix": "!"}

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
async def yt(ctx):
    await ctx.send("This is the RX channel: https://www.youtube.com/c/RrrrrrrXXX")

@bot.command()
async def insta(ctx):
    await ctx.send("This is the RX instagram: https://www.instagram.com/rrrrrrrxxx/")

@bot.command()
async def fb(ctx):
    await ctx.send("This is the RX facebook: https://www.facebook.com/rrrrrrrxxx ")


videos = ["https://youtu.be/tQMBkWg9lT0" , "https://youtu.be/AzexY8j70SE", "https://youtu.be/4K-XfEM_q3I","https://youtu.be/Ad9gLdgCnXE","https://www.youtube.com/watch?v=IF4ysmzhzDY&t=96s","https://www.youtube.com/watch?v=IqHf0PyXHD0&t=313s","https://www.youtube.com/watch?v=UanNY_631Ts&t=592s"  ] 

@bot.command()
async def rx(ctx):
    await ctx.send("I found a good video")
    await ctx.send(choice(videos))


@bot.command()
async def id(ctx):
    await ctx.send("Here is the Rrrrrrrxxx id on PUBG MOBILE \n562521606")

@bot.command()
async def pc(ctx):
    embed = discord.Embed(colour=0xFF0000,  description="CPU \nAMD Ryzen 9 3900X \n\nCooler\nWraith PRISM\n\nMotherboard\nMSI B450-A Pro Max\n\nMemory\nCorsair Vengeance LPX 32GB DDR4-3200MHz\n\nGPU\nMSI GeForce GTX 1080 Gaming X 8G\n\nCase\nNZXT H510i White\n\nStorage\nAdata XPG SX8200 Pro 512GB\n\nPSU\nCorsair TX-M Series TX650M 650W")
    embed.set_author(name="THE RX PC", icon_url="https://cdn.discordapp.com/avatars/344554922190045187/3b31373274342812417dbf5a0719f32f.webp?size=1024")
    embed.set_footer(text="© 2020-2021 RX BOT, all rights reserved.")
    await ctx.send(embed = embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(description= "This command does not Found \nenter your command correctly \nand see this channel <#781525304266850354> for more information\n\nThanks,", colour =0xFF0000)
        embed.set_author(name=f"{ctx.author.name}", icon_url=ctx.author.avatar_url)
        embed.set_footer(text="© 2020-2021 RX BOT, all rights reserved.")
        await ctx.send(embed=embed)
        await ctx.message.add_reaction("❌")
        return


bot.run(token)