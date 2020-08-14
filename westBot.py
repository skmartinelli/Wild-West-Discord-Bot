import discord
from discord.ext.commands import Bot


YOURTOKEN = "NzQzOTE2NTY4MjY1ODgzODAw.XzboSw.vS71tPOMepkoNdb--NSdJWcoCpY"

client = discord.Client()

@client.event
async def on_ready():
    print("Bot is ready")

@client.event
async def on_message(message):
    #message stuff
    if "!greeting" in message.content:
        await message.channel.send("howdy!")

client.run(YOURTOKEN)