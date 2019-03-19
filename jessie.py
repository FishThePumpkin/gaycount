import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
import os

client = commands.Bot(command_prefix = "-")
client.remove_command('help')
status = ['RockyxRachel','Jessie is gay','bitch lasagne','1x1=2']
gays = ['gay','gai','gae','gey','gei','gya']
IDs = {
    "Jessie": "290419231734890497",
    "Vivian": "346924005997019139",
    "Owner": "246437474463776769"
}
permissions = [IDs["Vivian"],IDs["Owner"]]

f = open("counters.txt","r")
jessie = f.readline()
f.close()
jessie = int(jessie)

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
    global jessie
    global IDs
    global gays
    mess = message.content.lower()
    for a in gays:
        if a in mess:
            if message.author.id == IDs["Jessie"]:
                #jessie += 1
                await client.send_message(message.channel, '**+1**')
                with open("counters.txt","r+") as f:
                    f_contents = f.readline()
                    new_contents = int(f_contents) + 1
                    f.seek(0)
                    f.write(str(new_contents))
                break
    
    if mess == 'jessie is gay':
            await client.send_message(message.channel, "Jessie has said gay %d times" % jessie) 
            
    if mess == 'jessie said gay':
        for b in permissions:
            if message.author.id == b:
                await client.send_message(message.channel, ":white_check_mark: **+1**")
                with open("counters.txt","r+") as f:
                    f_contents = f.readline()
                    new_contents = int(f_contents) + 1
                    f.seek(0)
                    f.write(str(new_contents))
                #jessie += 1
                break
    if mess == 'writetofile':
        with open("counters.txt","r+") as f:
            f_contents = f.readline()
            new_contents = int(f_contents) + 1
            f.seek(0)
            f.write(str(new_contents))
            print(f_contents, end = '')
            print(new_contents)
            f.seek(0)
            f_contents = f.readline()
            print(f_contents)
        
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
