#to turn bot on, python main.py in terminal
#ctrl c to stop it


import discord

from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bot = commands.Bot(command_prefix='>')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()  #This makes it listen for a specific command and will reply with 'await'
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def bottles_of_beer(ctx):
    text_block = ""

    for beer_count in range(99, -1, -1):
        if beer_count >=2:
           text_block += f"{i} bottles of beer on the wall, {i} bottles of beer.  Take one down, pass it around, {i}, bottles of beer on the wall."
        elif beer_count ==1:
           text_block += f"{i} bottles of beer on the wall, {i} bottles of beer.  Take one down, pass it around, {i}, bottles of beer on the wall." 
        elif beer_count < 1:
           text_block += ("No more bottles of beer on the wall.  :(")  #This produces a huge string

    text_block_array = [text_block[i:i+400] for i in range(0, len(text_block), 400)] #This turns the string into a list and limits it to 400 characters

    for block in text_block_array: 
        await ctx.send(block)

#if I say hello to the bot, how will it @ back at me
#@bot.listen()
#async def on_message(message):
    #if message.content.startswith('dio'): #message.content.startswith means that it listens for a message that starts with the text in the string
        #await message.reply('https://media.comicbook.com/2020/10/jojo-dio-brando-cosplay-1241185-1280x0.jpeg', mention_author=True)

@bot.listen()
async def on_message(message):
    if message.author.id == bot.user.id: # this will make the bot ignore its own commands
        return
    if "dio" in message.content.lower(): #message.content.startswith means that it listens for a message that starts with the text in the string
        await message.reply('https://media.comicbook.com/2020/10/jojo-dio-brando-cosplay-1241185-1280x0.jpeg', mention_author=True)


@bot.listen()
async def on_message(message):
    if message.author.id == bot.user.id: # this will make the bot ignore its own commands
        return
    if "sekiro" in message.content.lower(): #message.content.startswith means that it listens for a message that starts with the text in the string
        await message.reply('Fuck Sekiro', mention_author=True)


@bot.listen()
async def on_message(message):
    if message.author.id == bot.user.id: # this will make the bot ignore its own commands
        return
    if "kingdom hearts" in message.content.lower(): #message.content.startswith means that it listens for a message that starts with the text in the string
        await message.reply('originally had physically forms but cast them off in order to attack hearts directly, infecting and possessing many people and propagating more formless shadows like themselves. However, as time passed and Darknesss numbers grew, peoples hearts began to birth darkness on their own through negative emotions, eventually giving rise to the Pureblood Heartless. ', mention_author=True)


bot.run(getenv("DISCORD_API_KEY"))

