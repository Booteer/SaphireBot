import discord
from discord.ext import commands, tasks
from config import *
import random
bot = ['Орёл', 'Решка']
numbers = ['1', '2', '3', '4', '5', '6']
asac = ['Да', 'Нет', 'Определённо нет', 'Определённо да ', 'Я не знаю, попробуй позже', 'Карты говорят нет', 'Карты говорят да', 'Звёзды говорят нет', 'Звёзды говорят да']
bot_choice = ['Камень', 'Ножницы', 'Бумага']
@client.command()
async def oreshka(ctx):
    nb = random.choice(bot)
    user = random.choice(bot)
    n = discord.Embed(title='Орёл или решка?', color=0xffe227)
    n.add_field(name='Вам выпал(а):', value=f'{user}')
    n.add_field(name = 'Боту выпал(а):', value = f'{nb}')
    await ctx.send(embed=n)
@client.command()
async def cube (ctx):
    bot1 = random.choice(numbers)
    num = random.choice(numbers)
    if bot1 > num:
        j = discord.Embed(title='Игра в кубик', color=0x64dfdf)
        j.add_field(name='Вам выпало число:', value=f'{num}', inline= False)
        j.add_field(name = 'Боту выпало:', value = f'{bot1}', inline = False)
        j.add_field(name = 'Выиграл', value = 'бот!', inline= False)
        await ctx.send(embed=j)
    if num > bot1:
        j = discord.Embed(title='Игра в кубик', color=0x64dfdf)
        j.add_field(name='Вам выпало число:', value=f'{num}', inline= False)
        j.add_field(name = 'Боту выпало:', value = f'{bot1}', inline = False)
        j.add_field(name = 'Выиграл', value = f'{ctx.message.author}', inline= False)
        await ctx.send(embed = j)
    if num == bot1:
        j = discord.Embed(title='Игра в кубик', color=0x64dfdf)
        j.add_field(name='Вам выпало число:', value=f'{num}', inline= False)
        j.add_field(name = 'Боту выпало:', value = f'{bot1}', inline = False)
        j.add_field(name = 'Выиграла ничья!', value = f'Уху!', inline= False)
        await ctx.send(embed = j)





@client.command()
async def gadanie(ctx, *, args):
    gadalka = random.choice(asac)
    q = discord.Embed(title='Предсказание', color=0x6930c3)
    q.add_field(name='Текст Предсказания:', value=f'{gadalka}')
    await ctx.send(embed=q)
@gadanie.error
async def gadalka_ne_mojet_naiti_answer(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        g = discord.Embed(title='Ошибка!', color=0xff060e)
        g.add_field(name='Причина ошибки:', value='Я не могу гадать по пустым сообщениям!', inline=False)
        g.add_field(name='Пример использования команды:', value=f'{prefix}gadanie я программистер?', inline=False)
        await ctx.send(embed=g)



    
    

    
