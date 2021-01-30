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
    n = discord.Embed(title='Орёл или решка?', color=0x8B4513)
    n.add_field(name='Вам выпал(а):', value=f'{user}')
    n.add_field(name = 'Боту выпал(а):', value = f'{nb}')
    await ctx.send(embed=n)
@client.command()
async def cube (ctx):
    bot1 = random.choice(numbers)
    num = random.choice(numbers)
    if bot1 > num:
        j = discord.Embed(title='Игра в кубик', color=0x6C12C1)
        j.add_field(name='Вам выпало число:', value=f'{num}', inline= False)
        j.add_field(name = 'Боту выпало:', value = f'{bot1}', inline = False)
        j.add_field(name = 'Выиграл', value = 'бот!', inline= False)
        await ctx.send(embed=j)
    if num > bot1:
        j = discord.Embed(title='Игра в кубик', color=0x6C12C1)
        j.add_field(name='Вам выпало число:', value=f'{num}', inline= False)
        j.add_field(name = 'Боту выпало:', value = f'{bot1}', inline = False)
        j.add_field(name = 'Выиграл', value = f'{ctx.message.author}', inline= False)
        await ctx.send(embed = j)
    if num == bot1:
        j = discord.Embed(title='Игра в кубик', color=0x6C12C1)
        j.add_field(name='Вам выпало число:', value=f'{num}', inline= False)
        j.add_field(name = 'Боту выпало:', value = f'{bot1}', inline = False)
        j.add_field(name = 'Выиграла ничья!', value = f'Уху!', inline= False)
        await ctx.send(embed = j)





@client.command()
async def gadanie(ctx, *, args):
    gadalka = random.choice(asac)
    q = discord.Embed(title='Предсказание', color=0xEB0C62)
    q.add_field(name='Текст Предсказания:', value=f'{gadalka}')
    await ctx.send(embed=q)
@gadanie.error
async def gadalka_ne_mojet_naiti_answer(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        g = discord.Embed(title='Ошибка!', color=0xff060e)
        g.add_field(name='Причина ошибки:', value='Я не могу гадать по пустым сообщениям!', inline=False)
        g.add_field(name='Пример использования команды:', value=f'{prefix}gadanie я программистер?', inline=False)
        await ctx.send(embed=g)

@client.command()
async def knb (ctx, arg: str):
    botik = random.choice(bot_choice)
    if botik == 'Бумага' and arg == 'Бумага':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграла', value = 'ничья!')
        await ctx.send(embed = em)
    if botik == 'Камень' and arg == 'Камень':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграла', value = 'ничья!')
        await ctx.send(embed = em)
    if botik == 'Ножницы' and arg == 'Ножницы':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграла', value = 'ничья!')
        await ctx.send(embed = em)
    if botik == 'Камень' and arg == 'Ножницы':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'бот!')
        await ctx.send(embed = em)
    if botik == 'Камень' and arg == 'Бумага':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'пользователь!')
        await ctx.send(embed = em)
    if botik == 'Бумага' and arg == 'Ножницы':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'пользователь!')
        await ctx.send(embed = em)
    if botik == 'Бумага' and arg == 'Камень':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'бот!')
        await ctx.send(embed = em)
    if botik == 'Ножницы' and arg == 'Камень':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'пользователь!')
        await ctx.send(embed = em)
    if botik == 'Ножницы' and arg == 'Бумага':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'бот!')
        await ctx.send(embed = em)
    if botik == 'Бумага' and arg == 'бумага':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграла', value = 'ничья!')
        await ctx.send(embed = em)
    if botik == 'Камень' and arg == 'камень':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграла', value = 'ничья!')
        await ctx.send(embed = em)
    if botik == 'Ножницы' and arg == 'ножницы':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграла', value = 'ничья!')
        await ctx.send(embed = em)
    if botik == 'Камень' and arg == 'ножницы':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'бот!')
        await ctx.send(embed = em)
    if botik == 'Камень' and arg == 'бумага':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'пользователь!')
        await ctx.send(embed = em)
    if botik == 'Бумага' and arg == 'ножницы':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'пользователь!')
        await ctx.send(embed = em)
    if botik == 'Бумага' and arg == 'камень':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'бот!')
        await ctx.send(embed = em)
    if botik == 'Ножницы' and arg == 'камень':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'пользователь!')
        await ctx.send(embed = em)
    if botik == 'Ножницы' and arg == 'бумага':
        em = discord.Embed(title = 'Камень, ножницы, бумага!')
        em.add_field(name = 'Вы выбрали:', value = f'{arg}')
        em.add_field(name = 'Бот выбрал:', value = f'{botik}')
        em.add_field(name = 'Выиграл', value = 'бот!')
        await ctx.send(embed = em)
      

@knb.error
async def kbn_err(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        g = discord.Embed(title='Ошибка!', color=0xff060e)
        g.add_field(name='Причина ошибки:', value='Выберите: ножницы / бумага / камень!', inline=False)
        g.add_field(name='Пример использования команды:', value=f'{prefix}kbn камень', inline=False)
        await ctx.send(embed=g)

    
    

    
