import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix="/")
client = discord.Client()
@client.event
async def on_ready():
    print('--------------------')
    print(client.user.name)
    print(client.user.id)
    print('--------------------')

@client.event
async def say(ctx, *, say : str):
    """Echoooooo...."""
    if message.author == client.user:
        return
    
    await bot.delete_message(ctx.message)
    await bot.say(say)

@client.event
async def add(left : int, right : int):
    """Adds Numbers, what else?"""
    if message.author == client.id:
        return
    await bot.say(left + right)

@client.event
async def subtract(left : int, right : int):
    """Subtracts Numbers, if you don't know how to."""
    if message.author == client.id:
        return
    await bot.say(left - right)

@client.event
async def multiply(left:int,right:int):
    """Multiply Numbers, BASIC!"""
    if message.author == client.id:
        return
    await bot.say(left*right)

@client.event
async def divide(left:int,right:int):
    """Divides Numbers, like food"""
    if message.author == client.id:
        return
    await bot.say(left/right)

@client.event
async def repeat(times : int, text='repeating...'):
    """It's in the word you grade school or something?"""
    if message.author == client.id:
        return
    
    for i in range(times):
        await bot.say(text)

@client.event
async def trap(ctx, *, member :discord.Member = None):
    """Says if user is a trap. """
    if message.author == client.user:
        return
    
    if member is None: 
        await bot.say("Please input a username using the @ sign.")
        return    
    if member.id == "173654165434793984":
        await bot.say(" Hime!, Trap confirmed!".format(ctx))
    elif member.id == '170063603548815360':
        await bot.say(' Astolfo?, Trap confirmed.'.format(ctx))

@client.event
async def coin(choices = (['Heads', 'Tails'])):
    """Chooses between Heads or Tails."""
    if message.author ==client.user:
        return
    await bot.say("Flipping!")
    await bot.say(random.choice(choices))

@client.event
async def fortune(Fortunes = (["Today it's up to you to create the peacefulness you long for.","A friend asks only for your time not your money.","If you refuse to accept ,anything but the best, you very often get it.","A smile is your passport into the hearts of others.","A good way to keep healthy is to eat more Chinese food.","Your high-minded principles spell success.","Hard work pays off in the future, laziness pays off now.","Change can hurt, but it leads a path to something better.","Enjoy the good luck a companion brings you.","People are naturally attracted to you.","Hidden in a valley beside an open stream- This will be the type of place where you will find your dream.","A chance meeting opens new doors to success and friendship.","You learn from your mistakes... You will learn a lot today.","If you have something good in your life, don't let it go!","What ever you're goal is in life, embrace it visualize it, and for it will be yours."])):
    """A list of Fortunes"""
    if message.author == client.user:
        return
    
    await bot.say(random.choice(Fortunes))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('trap'):
        await client.send_message(message.channel, 'Trap?.... Who?')
        
    if message.content.startswith('hello'):
        await client.send_message(message.channel, message.author.mention+' Hello There')

    if message.content.startswith('Astolfo is life'):
        await client.send_message(message.channel, 'Hello')

    if message.content.startswith('Im still loyal to Astolfo'):
        await client.send_message(message.channel, message.author.mention+' What about Saya? tht russian chick.')

    if message.content.startswith('De_pressed'):
        await client.send_message(message.channel, 'Hello')

    if message.content.startswith('Edgy'):
        await client.send_message(message.channel, 'Hello')

    if message.content.startswith('Ass'):
        await client.send_message(message.channel, 'Hello')

    if message.content.startswith('Aye'):
        await client.send_message(message.channel, 'Aye!')

    if message.content.startswith('Kill yourself'):
        await client.send_message(message.channel, 'Hello')

    if message.content.startswith('Traps are not gay'):
        await client.send_message(message.channel, ' It aint gay if you say no homo.')

    if message.content.startswith('I wanna kill myself'):
        await client.send_message(message.channel, 'Hello')


client.run ("Mzk0NzgwNjgyNDAyMTM2MDY1.DSJTww.YcWmxyE23vLCcRO0iX2duxL5AxA")
