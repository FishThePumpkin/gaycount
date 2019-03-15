import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
import os

client = commands.Bot(command_prefix = "-")
client.remove_command('help')
status = ['Cat\'s', 'voice', 'is', 'so', 'nice', 'owo']
jessie = 1

async def change_status():
    await client.wait_until_ready()
    msgs = cycle(status)
    
    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(2)


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='Online!'))
    print("Bot is ready")

@client.event
async def on_message(message):
    if 'gay' in message.content:
                        #290419231734890497
        global jessie
        jessie += 1
        print('gay')
        await client.say('Jessie said gay')

@client.command()
async def ping():
    await client.say('Pong!')

@client.command()
async def jessiegay():
    await client.say("Jessie has said gay %d times" % jessie)

@client.command(pass_context=True)
async def help(ctx):

    embed = discord.Embed(
        color = discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='**-ping**', value='Returns Pong!', inline=False)
    
    embed.add_field(name='**-say <string>**', value='Tells the bot to say something.', inline=False)
    

    await client.say(embed=embed) #send_message(author, embed=embed)


    
@client.command()
async def say(*args):
    output = ' '
    for word in args:
        output += word
        output += ' '
    await client.say(output)
    
    
    
client.loop.create_task(change_status())
client.run(os.environ['BOT_TOKEN'])    
