import discord
from discord.ext import commands
import asyncio

bot =                                                                   commands.Bot(command_prefix='D'          )

@bot.event
async def on_ready():
	print('The bot is ready!')
	print(bot.user.name)
	print(bot.user.id)
	
bot.run('NTIwMTIxNTY3NDkwMDgwNzY4.DupRgw.rsqoaG625Eq6vgZZE30GNN8XkUY')
