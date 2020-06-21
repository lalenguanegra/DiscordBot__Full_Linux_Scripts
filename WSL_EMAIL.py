import discord
import sys
import subprocess 
from subprocess import call
from discord.ext import commands
bot = commands.Bot(command_prefix='!')

@bot.command()
async def ayy(ctx, arg):
    await ctx.send("Please Wait...")
    text_file = open("URL.txt", "a")  
    text_file.write(arg+"\n")
    await ctx.send(arg + " was added!")


@bot.command()
async def go(ctx):
    await ctx.send("Loading...")
    subprocess.call('python3 ./YT.py', shell=True)
    await ctx.send("downloaded!")

@bot.command()
async def email(ctx):
    await ctx.send("Sending Email...")
    subprocess.call('python3 ./Send_Media.py', shell=True)
    await ctx.send("SENT!")

@bot.command()
async def gone(ctx):
    await ctx.send("Deleted...")
    subprocess.call('python3 ./DEL.py', shell=True)
bot.run('token')