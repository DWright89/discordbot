#to turn bot on, python main.py in terminal
#ctrl c to stop it

# git add (the files you want to add)
# git commit -m "Name of change"
# git push
# git pull to synchronize changes from elsewhere

import discord
import random

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
########
# 3n+1 #
########
def check_even(input) -> bool:
    """
    Returns whether a interger is even or odd 
    """
    quotient = (input % 2)
    #print('checking if even')
    if quotient == 0:
        return True
    else:
        return False
    
def divide_by_2(input):
    """
    Takes in an integer and divides it by two
    """
    quotient = (input/2)
    #print('dividing by two')
    print(quotient)
    return quotient

def times_three_plus_one(input):
    """
    Takes in an integer and multiplies it by three, adding one
    """
    #print('times 3 + 1')
    product = (input * 3) + 1
    print(product)
    return product 


@bot.command()
async def three_n_plus_one(ctx, message):
        text_block= ""
        print(message)        
        working_input = int(message)
        while working_input != 1:
            if check_even(input=working_input):
                working_input = divide_by_2(input=working_input) 
                text_block += f"{working_input}, "
            else:
                working_input = times_three_plus_one(input=working_input)
                text_block += f"{working_input}, "

        text_block_array = [text_block[i:i+400] for i in range(0, len(text_block), 400)]
        for block in text_block_array: 
            await ctx.send(block)  

@bot.listen()
async def on_message(message):
    if message.author.id == bot.user.id: # this will make the bot ignore its own commands
        return
    if "dio" in message.content.lower(): #message
    #.content.startswith means that it listens for a message that starts with the text in the string
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



fortune_list = ["You will find vague joy", "If you work hard, something will happen", "Your future looks like your past", "Just tell yourself it isn't your fault",
                "A glizzy in the throat is worth two on the grill", "Your best is not good enough", "There will come a day when your lack of preparation will not pay off",
                "Try being more proactive with your hygiene", "Ugggggghhhhhh", "There is a promotion on the horizon for someone else", "This service is no more or less accurate than a 'professional'",
                "Settling down is just another form of settling", "If you push the people around you to be their best, wait until they break first and pick up their shifts for overtime", 
                "Start a business by stealing the labor of your friends", "Hide behind someone more competent than you and try to take credit for their work", "The sun never sets on someone traveling west at ~1,200mph",
                "Tell someone they're good enough without lying to make yourself feel morally justified for what you're about to do", "Your minimalist approach to having a work ethic isn't impressing anyone",
                "No matter how hard you work, you'll never make something better than Bloodborne", "Trick yourself and those around you into believing that you are happy"]

@bot.command()
async def tell_fortune(ctx):
    fortune_result = ""
    user_number = random.randint(1,len(fortune_list)) - 1
    fortune_result += f"{fortune_list[user_number]}"
    await ctx.send(fortune_result)



