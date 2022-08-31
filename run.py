# Works with Python 3.6+
import discord
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
print(discord.__version__)
import asyncio
import json
import sys

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="m.", intents=intents)

with open('config.json', 'r') as f:
    config = json.load(f)

TOKEN = config['token']

bot.help_command = None

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
# wHY THE FUCK ARE U LOOKING HERE THO?
# made with <3 for 2 hours
        
@bot.command()
async def help(ctx):    
    embed=discord.Embed()
    embed.set_author(name="Help?", url="https://www.mcl.edu.ph/list-of-faculty/", icon_url="https://i.imgur.com/YkQy0SY.png")
    embed.add_field(name="What is Glenda?", value="**Glenda** is a proud shs *princi-* **bot** ", inline=False)
    
    embed.add_field(name="Want to anonymously confess?", value="**DM** me 'm.confess [confession/attachment]' or 'm.confession [confession/attachment]' without the 'quotes' and [brackets]", inline=False)
    embed.add_field(name="Notes:", value="Glenda can accept attachments such as images, videos and gifs below 10mb.\n**Do not use the m.confess command outside Glenda's DM**", inline=False)
    embed.add_field(name="Curious on how Glenda works?", value="**Glenda** uses *discord.py* to handle stuff | Check out the GitHub Repo~: https://github.com/JGabT/Glenda", inline=False)
    
    await ctx.send(embed=embed)
        
@bot.command()
async def confess(ctx, *, message, member: discord.Member = None):
    member = member or ctx.author
    conf_file = 'confessions.txt'
    conf = bot.get_channel(1014149217490567209)
    admin = bot.get_channel(1014165254743269458)
    
    with open(conf_file) as f:
        count = f.readlines()
        conf_count = int(count[0])
        print(conf_count)
            
    with open(conf_file, 'w') as filetowrite:
        conf_count = str(int(count[0]) + 1)
        print(conf_count)
        filetowrite.write(conf_count)
        
    embed=discord.Embed(title=str(message))
    embed.set_author(name=f"Anonymous Confession #{conf_count}", url="https://mcl.edu.ph", icon_url="https://i.imgur.com/YkQy0SY.png")
    embed.set_footer(text="Want to confess? DM me 'm.confess [confession/attachment]' without the 'quotes' and [brackets]")
    
    await ctx.send(f'Successfully sent your confession!~ | #{conf_count}')
    await conf.send(embed=embed)
    await admin.send(f"'anonymous' author: {member.mention}", embed=embed)
    
@bot.command()
async def confession(ctx, *, message, member: discord.Member = None):
    member = member or ctx.author
    conf_file = 'confessions.txt'
    conf = bot.get_channel(1014149217490567209)
    admin = bot.get_channel(1014165254743269458)
    
    with open(conf_file) as f:
        count = f.readlines()
        conf_count = int(count[0])
        print(conf_count)
            
    with open(conf_file, 'w') as filetowrite:
        conf_count = str(int(count[0]) + 1)
        print(conf_count)
        filetowrite.write(conf_count)
        
    embed=discord.Embed(title=str(message))
    embed.set_author(name=f"Anonymous Confession #{conf_count}", url="https://mcl.edu.ph", icon_url="https://i.imgur.com/YkQy0SY.png")
    embed.set_footer(text="Want to confess? DM me 'm.confess [confession/attachment]' without the 'quotes' and [brackets]")
    
    await ctx.send(f'Successfully sent your confession!~ | #{conf_count}')
    await conf.send(embed=embed)
    await admin.send(f"'anonymous' author: {member.mention}", embed=embed)
    
# Handle attachments pls?


bot.run(TOKEN)