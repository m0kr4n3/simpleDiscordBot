import os
from dotenv import load_dotenv
import discord
from discord.ext import commands 

load_dotenv()

token = os.environ.get('DISCORD_TOKEN')

bot = commands.Bot(command_prefix="$")


@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord")


@bot.event
async def on_command_completion(ctx):
    command = ctx.command.qualified_name
    guild_name = ctx.guild.name
    author = ctx.message.author
    print(f'Executed \"${command}\" command in {guild_name} by {author}')

@bot.command(name='hello',help="says hello world")
async def hello(ctx):
    await ctx.send("Hi, what's your name ?")
    name = await bot.wait_for('message',timeout=60,
                    check=lambda message:message.author.id == ctx.message.author.id)
    
    message = f"Nice to meet you {name.content}"
    embedded_message = discord.Embed(title=message,description='',color=0x00FF00)
    
    await ctx.send(embed=embedded_message)


@bot.command(name='mul',help="multiply 2 numbers")
async def mul(ctx,a :int,b:int):
    result = str(a * b)
    await ctx.send(f"The result is {result}")

@bot.command(name='add_channel',help="creates a new text channel")
@commands.has_role('admin')
async def add_channel(ctx, channel_name: str):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        await guild.create_text_channel(channel_name)
        message = f"{channel_name} channel has been successfully created!"
        print(message)
        await ctx.send(message)
    #await ctx.send(message)



bot.run(token)