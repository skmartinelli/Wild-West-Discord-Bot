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
        startcase = random.randint(0,2)
        user = message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await message.channel.send("User is in the channel: " + channel)
            vc = await voice_channel.connect()
            
            
            
            vc.play(discord.FFmpegPCMAudio('goodbadugly.mp3'), after=lambda e: print('done', e))
            while vc.is_playing():
                await asyncio.sleep(1)
            vc.stop()
            await vc.disconnect()
        
        
        
        else:
            await client.say("User is not in a voice channel")

    if "!moo" in message.content:
        index = 0
        cutoff = 3
        user = message.author
        voice_channel = user.voice.channel
        channel = None
        if voice_channel != None:
            channel = voice_channel.name
            await message.channel.send("User is in the channel: " + channel)
            vc = await voice_channel.connect()
            vc.play(discord.FFmpegPCMAudio('moo.mp3'), after=lambda e: print('done', e))
            while vc.is_playing():
                if index < cutoff:
                    await asyncio.sleep(1)
                else:
                    vc.stop()
                index += 1
            vc.stop()
            await vc.disconnect()
        else:
            await client.say("User is not in a voice channel")


client.run(YOURTOKEN)
