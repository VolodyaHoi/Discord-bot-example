import random # libs
import discord
from discord.ext import commands

config = { # config
    'token': 'your token', # bot`s token from discord developing site
    'prefix': '$', # commands tag ( $help )
}

intents = discord.Intents.default() # permissions

client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix=config['prefix'], intents=intents) # configure

@bot.command() # command $rand - got random number (0, 100)
async def rand(ctx, *arg):
    await ctx.reply(random.randint(0, 100)) # result in reply
    
@bot.command() # command $hello - bot send "hello" message ( without reply )
async def hello(ctx):
    await ctx.send("Hello bro!") # send message

bot.run(config['token']) # start bot
