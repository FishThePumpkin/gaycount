import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import time
import random
from random import *
import os

client = commands.Bot(command_prefix = "-")
client.remove_command('help')
status = ['RockyxRachel','Jessie is gay','bitch lasagne','1x1=2']
gays = ['gay','gae','gey','gei','gya']
imnot = ["i'm not","im not","i’m not","i am not"]
IDs = {
    "Jessie": "290419231734890497",
    "Vivian": "346924005997019139",
    "Owner": "246437474463776769",
    "Bot": "556089994708779033",
    "Rachel": "318366307169075201",
    "Labib": "378820414350295040"
}
permissions = [IDs["Vivian"],IDs["Owner"]]
imnotPERMS = [IDs["Rachel"],IDs["Labib"]]
jessie = 261

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
    auth = message.author.id
    authname = message.author
    authid = str(auth)
    mess = message.content.lower()
    channel = message.channel
    lotto = randint(1,10000)
    print("%s %s %d" % (authname,channel,lotto))
    if lotto == 1004:  
        await client.send_message(message.channel, "**OH MY GOD** <@%s> **JUST ROLLED A 1004 OUT OF 10000 POSSIBLE NUMBERS%s** **THAT'S A WOPPING 0.01%s%s** **GIVE** <@%s> **AN APPLAUSE%s** :clap::clap::clap: (You must say Jessie is gay now.)" % (authid,"!","%","!",authid,"!!!!!"))
    for a in gays:
        if a in mess:
            if message.author.id == IDs["Jessie"]:
                jessie += 1
                await client.send_message(message.channel, '**+1**')
                break
    #yes
    if mess == 'jessie is gay':
            await client.send_message(message.channel, "Jessie has said gay %d times" % jessie) 
            
            
    if mess == 'jessie said gay':
        for b in permissions:
            if message.author.id == b:
                await client.send_message(message.channel, ":white_check_mark: **+1**")
                jessie += 1
                break
    if mess == 'fireworks':

        await client.send_message(message.channel,':sparkler:')
        await client.send_message(message.channel,':fireworks:')
        await client.send_message(message.channel,':milky_way:')
        
    if not message.author.id == IDs["Bot"]:
        for c in imnot:
            if c in mess:
                for d in imnotPERMS:
                    if message.author.id == d:
                        chars = mess.split()
                        #print(chars)
                        joinedmess = ' '
                        for i in range (0, len(chars)):
                            if chars[i] == "not":
                                #print(i)
                                #await client.send_message(message.channel, chars[i])
                                a = i + 1
                                if a == len(chars):
                                    joinedmess = " not "
                                    break
                                for j in range (a, len(chars)):        
                                    joinedmess += chars[j]
                                    joinedmess += ' '
                                    #await client.send_message(message.channel, joinedmess)   
                                break
                        newMess = "It's not like I'm%sor anything..." % joinedmess
                        await client.send_message(message.channel, newMess)   
                        break
                
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
