import discord

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
        user = context.message.author
        voice_channel = user.voice.voice_channel
        channel = None
        if voice_channel != None
            channel = voice_channel.name
            await client.say("User is in the channel: " + channel)
            vc = await client.join)voice_channel(voice_channel)
            player = vc.create_ffmpeg_player('goodbadugly.mp3', after=lambda: print('done'))
            player.start()
            while not player.isdone():
                await asyncio.sleep(1)
            player.stop()
            await vc.disconnect()
        else:
            await client.say("User is not in a voice channel")



client.run(YOURTOKEN)