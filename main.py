import discord
from discord import utils
from discord.ext import commands
import os
# импорт библиотек


client = commands.Bot(command_prefix = '.')

# команда для очистки чата
@client.command()
async def clear(ctx, num = 5):
	await ctx.channel.purge(limit = num)

# авто-роль
@client.event
async def on_member_join(member):
	role = discord.utils.get(member.guild.roles, id=int("689396798879563843"))
	await member.add_roles(role)

@client.command()
async def info(ctx):
	members = message.guild.members
	for member in members:
		await ctx.send(member)
	
# прощание
@client.event
async def on_member_remove(member):
	channel = discord.utils.get(member.guild.channels, id=int("693815346502565898"))
	await channel.send(f"{member} 𝘭𝘦𝘧𝘵 𝘶𝘴. 𝘉𝘺𝘦 𝘉𝘺𝘦!")


# информация
@client.command()
async def info(ctx):
	await ctx.send("На этом дискорд сервере ты встретишь дружелюбных и адекватных людей,хорошую администрацию,Музыкального Бота и другое(над сервером ведётся работа,если есть идеи пишите а ЛС в Discord 𝓝𝓮𝓭_𝓝𝓮𝓭𝓸𝓿#2686)")
	
# RUN
token = os.environ.get('BOT_TOKEN')

client.run(str(token))
# в config.py нужен по сути только TOKEN,но на всякий случай,пусть все остается,как есть
