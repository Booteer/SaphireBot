import discord
from config import *
from discord.ext import commands, tasks
import asyncio
from utils import *
from roleplay import *
from game import *
from Cybernator import Paginator
from administration import *
client.remove_command('help')
@client.event
async def on_ready():
    print('Ого, ты удачно настроил меня! Я запущен!')
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f'Слежу за {len(client.guilds)} серверами.'))

@client.command()
async def help (ctx):
    em1 = discord.Embed(title = 'Игры:')
    em1.add_field(name = '(<> - обязательный аргумент! ; () - необязательный) \n Все игры в боте:', value = f'``{prefix}cube`` - подкинуть кубик \n ``{prefix}oreshka`` - орёл или решка \n ``{prefix}gadanie <text>`` - гадание.')
    em2 = discord.Embed(title = 'Roleplay:')
    em2.add_field(name = u'(<> - обязательный аргумент! ; () - необязательный) \n Все рп команды в боте:', value = f'``{prefix}hug (@user)`` - обнять пользователя \n ``{prefix}poke (@user)`` - тыкнуть пользователя \n ``{prefix}kiss (@user)`` - поцеловать пользователя \n ``{prefix}pat (@user)`` - погладить пользователя \n ``{prefix}tea (@user)`` - попить чаю с пользователем.')
    em3 = discord.Embed(title = 'Утилиты:')
    em3.add_field(name = u'(<> - обязательный аргумент! ; () - необязательный) \n Все утилиты в боте:', value = f'``{prefix}trans <language> <text>`` - переводчик \n ``{prefix}server_inform - информация о сервере`` \n ``{prefix}inform <@user>`` - информация о пользователе \n ``{prefix}weather <москва>`` - погода \n ``{prefix}shortlink <link.com>`` - сокращение ссылки \n ``{prefix}wikipedia <статья>`` - поиск по википедии \n ``{prefix}cat / dog / anime / pikachu`` - рандомное изображение \n ``{prefix}stopgame`` - парсер с сайта stopgame \n ``{prefix}hentai`` - рандомное аниме NSFW изображение / гифка \n ``{prefix}ping`` - пинг бота')
    embeds = [em1, em2, em3]
    p = await ctx.send(embed = em1)
    page = Paginator(client, p, only=ctx.author, use_more=False, embeds=embeds)
    await page.start()
client.run(api_discord)
