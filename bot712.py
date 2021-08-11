import discord
from discord import channel
from discord import message
from discord.ext import commands
from discord.flags import Intents
import asyncio

intents=discord.Intents(members=True, messages=True, guilds=True, reactions = True)

bot=commands.Bot(command_prefix="(",intents=intents)

@bot.event
async def on_ready():
    print('>>Bot Is Online<<')


@bot.event
async def on_member_join(member):
    channel = bot.get_channel(857883822963687424)
    await channel.send(f'神奇的{member}加入了!')
#成員加入

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(857883822963687424)
    await channel.send(f'{member}你走了~~')
#成員離開

@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == "👌":
        print('ok')
        guild = bot.get_guild(857860268248137728)
        role = guild.get_role(874551280754896956)
        await payload.member.add_roles(role)
        

@bot.command()
async def ping(ctx):
    await ctx.send(f'{bot.latency*1000}ms')
#測網路

@bot.command()
async def hh(ctx,msg):
    await ctx.message.delete()
    await ctx.send(msg)

bot.run('ODYxNTA1OTE4ODc3MTcxNzEy.YOKx6Q.om9wHCZaoIt4tdvUaIIGFeSNVn8')