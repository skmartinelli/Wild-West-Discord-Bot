import discord
import asyncio
import random


from discord.utils import get
from discord.ext import commands

# My code is very very ugly and often sloppy :(
# I couldn't figure out how to define functions to use inside the async functions so next time I'd like to learn that
# However I am proud of myself for getting this all to work! New to building projects :D

YOURTOKEN = "NzQzOTE2NTY4MjY1ODgzODAw.XzboSw.qRX0rkF_0hdjBWpmYUg1bvyx2gc"

client = discord.Client()
vc = None
duelActive = False
postduel = False
isitmusic = False
timer = 0

# Timer and bot startup 
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


# I think there is a better way to do this because its a bunch of ugly ifs and elifs
@client.event
async def on_message(message):
    #message stuff
    if "!greeting" in message.content:
        await message.channel.send("howdy!")


    # Showdown time :D
    if "!showdown" in message.content:
        global vc
        global duelActive
        global isitmusic

        # pick one of the points to start song from
        startcase = random.randint(0,2)
        duelActive = True
        isitmusic = True
        user = message.author
        voice_channel = user.voice.channel
        channel = None
        if message.author.voice:
            channel = voice_channel.name
            await message.channel.send("A duel is beginning in " + channel + "...")
            
            if not vc:
                vc = await voice_channel.connect()
            
            # Play from beginning
            if startcase == 0:
                endDistances = [144.8, 166, 294.47]
                vc.play(discord.FFmpegPCMAudio('goodbadugly.mp3'), after=lambda e: print('done', e))
                length = random.choice(endDistances)
                length = 5
                await asyncio.sleep(length)
                vc.stop()

            # Play from one third in
            elif startcase == 1:
                endDistances = [150, 303]
                vc.play(discord.FFmpegPCMAudio('goodbadugly225.mp3'), after=lambda e: print('done', e))
                length = random.choice(endDistances)
                await asyncio.sleep(length)
                vc.stop()
            
            # Play from two thirds in
            elif startcase == 2:
                vc.play(discord.FFmpegPCMAudio('goodbadugly454.mp3'), after=lambda e: print('done', e))
                await asyncio.sleep(137.5)
                vc.stop()
        # If they aren't in a vc
        else:
            await client.say("You ain't in a voice channel!")

    if "!bang" in message.content:
       # YUCK 5 global variables. Here's what they do and why I need them
       # vc: vc is the object for the voice channel player and that's how i can check if the bot is making noise
       # duelActive: used to check if a duel is currently happening
       # postDuel: used to check if it's after a duel and not before
       # isitmusic: used to check if sound played is a gunshot or the music
       # timer: Probably could be combined with postDuel to see if it's directly after a duel but it looks ugly in my head to do it that way LOL
        global postduel
        global timer
        
        # If duel is happening (Music either playing or JUST ended)
        if duelActive: 
            if vc.is_playing() and isitmusic == True:
                await message.channel.send("You fired too early and lost the duel, you suck")
               
            else: #if vc is not playing, duel is either HAPPENING, hasn't started, or has already ended
                await message.channel.send("You won the duel :D")
                isitmusic == False
                vc.stop()
                duelActive = False
                postduel = True
                vc.play(discord.FFmpegPCMAudio('bang.mp3'), after=lambda e: print('done', e))
                timer = 5
        
        # Duel has not been started or 
        elif not duelActive and postduel == False:
            await message.channel.send("There's no duel happening!")
            vc.play(discord.FFmpegPCMAudio('bang.mp3'), after=lambda e: print('done', e))
            isitmusic == False
        
        # Duel has ended before timer runs out
        elif not duelActive and  postduel == True:
            await message.channel.send("You lost the duel")
            vc.play(discord.FFmpegPCMAudio('bang.mp3'), after=lambda e: print('done', e))
            isitmusic == False
                
            
    
    # make it stop!!!
    if "!dcwest" in message.content:
        await vc.disconnect()
    
    # Moo
    if "!moo" in message.content:
        cutoff = 5
        voice_channel = message.author.voice.channel 
        if message.author.voice:
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('moo.mp3'), after=lambda e: print('done', e))
            await asyncio.sleep(cutoff)
            vc.stop()
        else:
            await message.channel.send("You ain't  in a voice channel!")


client.run(YOURTOKEN)
