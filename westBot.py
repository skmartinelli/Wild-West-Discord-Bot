import discord
import asyncio
import random


from discord.utils import get
from discord.ext import commands


YOURTOKEN = "NzQzOTE2NTY4MjY1ODgzODAw.XzboSw.qRX0rkF_0hdjBWpmYUg1bvyx2gc"

client = discord.Client()


@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    #message stuff
    if "!greeting" in message.content:
        await message.channel.send("howdy!")

    if "!showdown" in message.content:
        global vc
        #startcase = random.randint(0,2)
        # XXX
        startcase = 0
        user = message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await message.channel.send("User is in the channel: " + channel)
            vc = await voice_channel.connect()
            
            
            if startcase == 0:
                endDistances = [145, 166, 294.47, 434]
                vc.play(discord.FFmpegPCMAudio('goodbadugly.mp3'), after=lambda e: print('done', e))
                

                #length = random.choice(endDistances)
                length = 144.8
                await asyncio.sleep(length)
                
                
                
                vc.stop()
                await vc.disconnect()

            
            elif startcase == 1:
                
                endDistances = [150, 306]
                vc.play(discord.FFmpegPCMAudio('goodbadugly225.mp3'), after=lambda e: print('done', e))
                
                length = random.choice(endDistances)
                await asyncio.sleep(length)
                
                vc.stop()
                await vc.disconnect()
        
            
            elif startcase == 2:
                vc.play(discord.FFmpegPCMAudio('goodbadugly454.mp3'), after=lambda e: print('done', e))
                
                
                await asyncio.sleep(137.5)
                
                
                vc.stop()
                await vc.disconnect()        
        # If they aren't in a vc
        else:
            await client.say("User is not in a voice channel")

    if "bang" in message.content:
        global vc
        if vc.is_playing():
            await message.channel.send("You fired too early and lost the duel, you suck")
        else:
            await message.channel.send("You won the duel :D")
    
    if "!moo" in message.content:
        # Set the index and the cutoff
        
        index = 0
        cutoff = 5
        user = message.author
        voice_channel = user.voice.channel
        channel = None
        
        # Connect to the voice channel
        if voice_channel != None:
            channel = voice_channel.name
            await message.channel.send("User is in the channel: " + channel)
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('moo.mp3'), after=lambda e: print('done', e))
            
            await asyncio.sleep(cutoff)
            
            vc.stop()
            await vc.disconnect()
        else:
            await client.say("User is not in a voice channel")


client.run(YOURTOKEN)
