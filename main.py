# импорт библиотек
import os
import discord
from discord import utils
from discord.ext import commands
import random

# client
client = commands.Bot(command_prefix='.')

# команда для очистки чата
@client.command()
async def clear(ctx, *,num=5):
	if int(num) > 250:
		await ctx.send("Слишком большое число")
	elif '+' in list(str(num)):
		await ctx.send('Неправильный ввод')
	else:
		await ctx.channel.purge(limit=num)
		

# авто-роль
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, id=int("689396798879563843"))
    await member.add_roles(role)

# прощание
@client.event
async def on_member_remove(member):
	channel = discord.utils.get(
	member.guild.channels, id=int("582894293551677451"))
	await channel.send(f"{member} 𝙡𝙚𝙛𝙩 𝙪𝙨! 𝘽𝙮𝙚 𝘽𝙮𝙚...")

# орел/решка игра
@client.command()
async def coin(ctx, args):
    variants = ['Орёл', 'Решка']
    if args == 'орел' or 'орёл':
        await ctx.send('Правильный ответ: ' + random.choice(variants))
    elif args == 'решка':
        await ctx.send('Правильный ответ: ' + random.choice(variants))

# представление
@client.command()
async def who(ctx):
    await ctx.send("Я Rudolf Hadler, помощник и бот на этом сервере.Всем хорошего дня и побед в играх!")

# помощь
@client.command()
async def helping(ctx, args):

    if args == 'server':
        await ctx.send("Для информации насчет ботов перейдите в Help. Для получения информации о каком-то канале,после комнады напиши назвние канала.")
    elif args == 'chat':
        await ctx.send("Этот канал для общения и разговоров")
    elif args == 'news':
        await ctx.send("Тут переодически появляются новости сервера")
    elif args == 'cheats':
        await ctx.send("Тут обмен читов для CS:GO")
    elif args == 'disscusion-cheats':
        await ctx.send("Тут обсуждение читов для CS:GO")
    elif args == 'help':
        await ctx.send("Это канал для получения информации о сервере")
    elif args == 'musicselect':
        await ctx.send("Канал для выбора песни для MusicRoom1")


# информация
@client.command()
async def info(ctx):
    await ctx.send("На этом дискорд сервере ты встретишь дружелюбных и адекватных людей,хорошую администрацию,Музыкального Бота и другое(над сервером ведётся работа,если есть идеи пишите а ЛС в Discord 𝐅𝐨𝐧𝐭𝐨𝐦𝐎𝐜𝐡𝐤𝐚#2686)")

# да/нет игра
@client.command()
async def askg(ctx, *,args):
        # warning = ['michael', 'jackson', 'Майкл, 'майкл', 'Michael', 'Jackson', 'MICHAEL', 'JACKSON', 'ДЖЕКСОН, 'МАЙКЛ']
        answers = ['Да','Возможно','Нет','Вероятнее всего','Может быть','Определённо нет','Определённо да', 'Не знаю','Не уверен','Дай минуту подумать']
        await ctx.send("Твой вопрос: " + args + "\nОтвет: " + random.choice(answers))


# RUN
token = os.environ.get('BOT_TOKEN')
client.run(str(token))
