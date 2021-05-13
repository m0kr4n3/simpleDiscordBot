import os
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord !')



@bot.command(name='mokrane',help='Responds any thing')
async def mokrane(ctx):
    respond = 'Hi I\'m Mokrane !'
    await ctx.send(respond)


@bot.command(name='mul',help='Multiplies a and b')
async def mul(ctx,a :int,b :int):
    await ctx.send(str(a*b))


@bot.command(name='create_channel',help='Creates a text channel (just for admins)')
@commands.has_role('admin')
async def create_channel(ctx,channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel :
        print(f'Creating a new channel: {channel_name}')
        await guild.create_text_channel(channel_name)

    
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')


bot.run(TOKEN)
