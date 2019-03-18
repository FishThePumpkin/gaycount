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
jessie = 129

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
    mess = message.content.lower()
    if 'gay' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            global jessie
            jessie += 1
            await client.send_message(message.channel, '**+1**')
    elif 'gae' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            await client.send_message(message.channel, '**+1**')
            jessie += 1
    elif 'gey' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            await client.send_message(message.channel, '**+1**')
            jessie += 1
    elif 'g@y' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            await client.send_message(message.channel, '**+1**')
            jessie += 1
    elif 'g@e' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            await client.send_message(message.channel, '**+1**')
            jessie += 1
    elif 'g a y' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            await client.send_message(message.channel, '**+1**')
            jessie += 1
    elif 'g ay' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            await client.send_message(message.channel, '**+1**')
            jessie += 1
    elif 'ga y' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gei' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gãi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gåi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gāi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gài' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gái' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gâi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gäi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gæy' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gya' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gėi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gęi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gēi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gêi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gèi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'géi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    elif 'gëi' in mess:
        if message.author.id == "290419231734890497":                  #290419231734890497
            jessie += 1
            #print('gay')
            await client.send_message(message.channel, '**+1**')
    
    if mess == 'jessie is gay':
        
            await client.send_message(message.channel, "Jessie has said gay %d times" % jessie) 
    if mess == 'jessie said gay':
        if message.author.id == "246437474463776769": #me
            await client.send_message(message.channel, ":white_check_mark: **+1**")
            jessie += 1
        elif message.author.id == "346924005997019139": #viv
            await client.send_message(message.channel, ":white_check_mark: **+1**")
            jessie += 1
            
@client.command()
async def ping():
    await client.say('Pong!')



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
