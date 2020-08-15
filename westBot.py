import discord
import asyncio
import random


from discord.utils import get
from discord.ext import commands


YOURTOKEN = "NzQzOTE2NTY4MjY1ODgzODAw.XzboSw.qRX0rkF_0hdjBWpmYUg1bvyx2gc"

client = discord.Client()
vc = None
duelActive = False
postduel = False
isitmusic = False
timer = 0
@client.event
async def on_ready():
    global timer
    global postduel
    print("Bot is ready")
    while True:
        timer -= 1
        await asyncio.sleep(1)
        if timer <= 0:
            postduel = False


@client.event
async def on_message(message):
    #message stuff
    if "!greeting" in message.content:
        await message.channel.send("howdy!")

    if "!showdown" in message.content:
        global vc
        global duelActive
        global isitmusic
        #startcase = random.randint(0,2)
        startcase = 1
        duelActive = True
        isitmusic = True
        user = message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await message.channel.send("User is in the channel: " + channel)
            
            if not vc:
                vc = await voice_channel.connect()
            
            
            if startcase == 0:
                endDistances = [144.8, 166, 294.47]
                vc.play(discord.FFmpegPCMAudio('goodbadugly.mp3'), after=lambda e: print('done', e))
                

                length = random.choice(endDistances)
                
                await asyncio.sleep(length)
                
                
                
                vc.stop()
                #await vc.disconnect()

            
            elif startcase == 1:
                
                endDistances = [150, 303]
                vc.play(discord.FFmpegPCMAudio('goodbadugly225.mp3'), after=lambda e: print('done', e))
                
                length = random.choice(endDistances)
                await asyncio.sleep(length)
                
                vc.stop()
                #await vc.disconnect()
        
            
            elif startcase == 2:
                vc.play(discord.FFmpegPCMAudio('goodbadugly454.mp3'), after=lambda e: print('done', e))
                
                
                await asyncio.sleep(137.5)
                
                
                vc.stop()
                #await vc.disconnect()    


        # If they aren't in a vc
        else:
            await client.say("User is not in a voice channel")

    if "!bang" in message.content:
        global vc
        global duelActive
        global postduel
        global isitmusic
        global timer
        
        if duelActive: 
            if vc.is_playing() and isitmusic == True:
                await message.channel.send("You fired too early and lost the duel, you suck")
               
            else: #if vc is not playing, duel is either HAPPENING, hasn't started, or has already ended
                await message.channel.send("You won the duel :D")
                vc.play(discord.FFmpegPCMAudio('bang.mp3'), after=lambda e: print('done', e))
                isitmusic == False
                vc.stop()
                duelActive = False
                postduel = True
                timer = 5
        elif not duelActive and postduel == False:
            await message.channel.send("There's no duel happening!")
            vc.play(discord.FFmpegPCMAudio('bang.mp3'), after=lambda e: print('done', e))
            isitmusic == False
        elif not duelActive and  postduel == True:
            await message.channel.send("You lost the duel")
            vc.play(discord.FFmpegPCMAudio('bang.mp3'), after=lambda e: print('done', e))
            isitmusic == False
                
            
            #await vc.disconnect()
    
    
    if "!disconnectWest" in message.content:
        await vc.disconnect()
    
    
    if "!moo" in message.content:
        # Set the index and the cutoff
        
        index = 0
        cutoff = 5
        user = message.author
        voice_channel = user.voice.channel
        channel = None
        
        # Connect to the voice channel
        if voice_channel is not None:
            channel = voice_channel.name
            await message.channel.send("User is in the channel: " + channel)
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('moo.mp3'), after=lambda e: print('done', e))
            
            await asyncio.sleep(cutoff)
            
            vc.stop()
            #await vc.disconnect()
        else:
            await message.channel.send("User is not in a voice channel")


client.run(YOURTOKEN)
