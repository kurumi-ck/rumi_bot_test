import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='~')

@bot.event
async def on_ready():
    print("bot is online")

bot.run("ODIxMzQyNjU3NTk4NDU1ODQ5.YFCU9Q.L_tmnHDv1n2-XadH7fERY6jaz-U")