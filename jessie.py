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
    "Labib": "378820414350295040",
    "Trung": "328345368494342155"
}
characterStats = {
    "Drater": [0,0,0,0,0,0,0],
    "Carla": [2,11,9,6,8,6,3],
    "Vivian": [6,6,8,6,7,7,5]
}
characterOwners = {
    "246437474463776769":"Drater",
    "556089994708779033":"Carla",
    "346924005997019139":"Vivian"
}
permissions = [IDs["Vivian"],IDs["Owner"]]
imnotPERMS = [IDs["Rachel"],IDs["Labib"]]
jessie = 372

inBattle = 0

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
    print("%s %s %d: %s" % (authname,channel,lotto,message.content))
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
    
    if 'battle' in mess:
         if not auth == IDs["Bot"]:
            for key in IDs:
                if mess == "battle <@%s>" % IDs[key]:
                    #await client.send_message(message.channel,"Battle begins.")
                    if auth in characterOwners:
                        if IDs[key] in characterOwners:
                            global inBattle               
                            await battle(message,characterOwners[auth],characterOwners[IDs[key]])
                            break  
                        else:
                            await client.send_message(message.channel,"This user does not have a character!")
                            return     
                    else:
                        await client.send_message(message.channel,"<@%s> You do not have a character!" % auth)
                        return                          
       
            #if message.author.id == IDs["Owner"]:
                #await battle(message,"Drater","Paula")
    
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

                  
async def battle(message,p1,p2):
    global inBattle
    mess = message.content.lower()
    p1auth = ""
    p2auth = ""
    for key in characterOwners:
        if characterOwners[key] == p1:
            p1auth = key
        elif characterOwners[key] == p2:
            p2auth = key
        if not p1auth == "" and p2auth == "":
            break
            
    
    if inBattle == 1:
        authid = message.author.id
        await client.send_message(message.channel,"<@%s> Another battle is already in progress. Try again later." % authid)
        return
    else:
        inBattle += 1
        await client.send_message(message.channel,"Battle begins between %s and %s" % (p1, p2))
        time.sleep(1)
        if p1 == "Drater" or p2 == "Drater": #Initialise stats for Drater
            await draterStats(1)

        p1Stats = characterStats[p1]
        p2Stats = characterStats[p2]
        #Base Damage
        p1Dmg = p1Stats[0]
        p2Dmg = p2Stats[0]
        #HP distribution
        p1Hp = p1Stats[1] * 3
        p2Hp = p2Stats[1] * 3
        p1Crit = 0
        p2Crit = 0
        #Capping crit
        if p1Stats[2] > 40:
            p1Crit = 40
        else:
            p1Crit = p1Stats[2]
        if p2Stats[2] > 40:
            p2Crit = 40
        else:
            p2Crit = p2Stats[2]
        p1Dodge = 0
        p2Dodge = 0
        #Dodge distribution
        p1Dodge = p1Stats[2] // 5
        p2Dodge = p2Stats[2] // 5

        currentMove = 0
        #First turn based on agility
        if p1Stats[3] > p2Stats[3]:
            await client.send_message(message.channel,"%s goes first!" % p1)
            time.sleep(1)
            currentMove = "p1"
        elif p1Stats[3] == p2Stats[3]:
            await client.send_message(message.channel,"Rolling dice...")
            time.sleep(1)
            rng = randint(0,1)
            if rng == 0:
                await client.send_message(message.channel,"%s goes first!" % p1)
                time.sleep(1)
                currentMove = "p1"
            else:
                await client.send_message(message.channel,"%s goes first!" % p2)
                time.sleep(1)
                currentMove = "p2"
        else:
            await client.send_message(message.channel,"%s goes first!" % p2)
            time.sleep(1)
            currentMove = "p2"

        #Fighting
        while not p1Hp <= 0 or p2Hp <= 0:
            if currentMove == "p1":
                currentturn = p1
                currentauth = p1auth
                currentdmg = p1Dmg
                currentcrit = p1Crit
                nextturn = p2
                nextdodge = p2Dodge
                nexthp = p2Hp
                nextmove = "p2"
            elif currentMove == "p2":
                currentturn = p2
                currentauth = p2auth
                currentdmg = p2Dmg
                currentcrit = p2Crit
                nextturn = p1
                nextdodge = p1Dodge
                nexthp = p1Hp
                nextmove = "p1"
                
            await client.send_message(message.channel,"Please make a move <@%s>" % currentauth)
            if message.author.id == currentauth:
                
                    rng = randint(0,100)
                    if rng in range(0,nextdodge): #Dodge Chance
                        await client.send_message(message.channel,"%s dodged the attack!" % nextturn)
                        time.sleep(1)

                    else: #Take damage
                        rng = randint(0,100)  
                        if rng in range(0,currentcrit): #Critical chance
                            damage = 1.5 * currentdmg
                            nexthp -= damage
                            await client.send_message(message.channel,"%s Crit!" % currentturn)
                            await client.send_message(message.channel,"%s dealt %d damage to %s, leaving them with %d HP remaining!" % (currentturn,damage,nextturn,nexthp))
                            time.sleep(1)
                        else: #Normal attack
                            nexthp -= currentdmg
                            await client.send_message(message.channel,"%s dealt %d damage to %s, leaving them with %d HP remaining!" % (currentturn,currentdmg,nextturn,nexthp))
                            time.sleep(1)
                    currentMove = nextmove
                        
            if p1Hp <= 0:
                await client.send_message(message.channel,"%s is the winner!" % p2)
                inBattle = 0
                break
            elif p2Hp <= 0:
                await client.send_message(message.channel,"%s is the winner!" % p1)
                inBattle = 0
                break
            

async def draterStats(pLvl):
    availablePts = 42 + pLvl 
    simpleStats = [0] * 7

    #Resetting Drater Stats for clean slate
    characterStats["Drater"] = [0] * 7    

    #Default base 1 for Con and Agi
    simpleStats[2] = 1
    simpleStats[6] = 1

    #Random point assignment
    for i in range(0,availablePts):
        rng = randint(0,51)
        if rng in range(0, 9): #Strength
            simpleStats[0] += 1
        elif rng in range(10, 19): #Constitution
            simpleStats[1] += 1
        elif rng in range(20, 29): #Dexterity
            simpleStats[2] += 1
        elif rng in range(30, 39): #Agility
            simpleStats[3] += 1
        elif rng in range(40, 49): #Charisma
            simpleStats[6] += 1
        elif rng == 50: #Intelligence
            simpleStats[4] += 1
        elif rng == 51: #Wisdom
            simpleStats[5] += 1

    stats = {
        "Strength": simpleStats[0],
        "Constitution": simpleStats[1],
        "Dexterity": simpleStats[2],
        "Agility": simpleStats[3],
        "Intelligence": simpleStats[4],
        "Wisdom": simpleStats[5],
        "Charisma": simpleStats[6],
        }
    characterStats["Drater"] = simpleStats 

async def saythis(messy):
    await client.send_message("general✤",messy)

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
