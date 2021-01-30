import discord
from discord.ext import commands, tasks
from googletrans import Translator
from config import *
import requests
from discord.ext.commands import MissingPermissions
import wikipedia
import requests
import json
from bs4 import BeautifulSoup
import pyshorteners
import nekos
import random
URL = 'https://stopgame.ru/news'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', 'accept':'*/*'}
link = 'https://stopgame.ru'
translator = Translator()


#Перводчик.
@client.command()
async def trans (ctx, lang,*, args):
    try:
        o = translator.translate(f'{args}', dest = f'{lang}')
    except Exception as e:
        # обработка исключения
        em = discord.Embed(title = 'Язык не найден!', color = 0xff060e)
        em.add_field(name = 'Пример использования команды:', value = f'{prefix}trans <lang>, <текст>', inline = False)
    else:
        em = discord.Embed(title = 'Переводчик.', color = 0xf8dc81)
        em.add_field(name = 'Оригинал текста:', value = f'{args}', inline = False)
        em.add_field(name = f'Перевод ({lang}):', value = f'{o.text}', inline = False)
    await ctx.send(embed = em)

@trans.error
async def trans(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        eb = discord.Embed(title = 'Ошибка!', color = 0xff060e)
        eb.add_field(name = f'Причина ошибки:', value = f'Не введён язык или текст! \n Пример использования: {prefix}trans <язык> <текст>')
        await ctx.send(embed = eb)
#Получаем информацию о пользователе.
@client.command(pass_context=True)
async def inform(ctx, member: discord.Member):
    dsf = discord.Embed(title='Информация о пользователе', color=0x8B008B)
    dsf.add_field(name='Когда зашёл на сервер:', value=member.joined_at, inline=False)
    dsf.add_field(name='Никнейм:', value=member.display_name, inline=False)
    dsf.add_field(name='id:', value=member.id)
    dsf.add_field(name='Дата регистрации:', value=member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC'))
    dsf.add_field(name = 'Аватарка:', value = '(секасная)', inline= False)
    dsf.set_image(url=member.avatar_url)
    dsf.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    dsf.set_author(name=ctx.message.author, url=ctx.message.author.avatar_url)
    await ctx.send(embed=dsf)

@inform.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите пользователя, чтобы узнать информацию!', inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}inform @user', inline=False)
        await ctx.send(embed=b)

#Получаем информацию о погоде.

@client.command()
async def weather(ctx, *, args):
    city_name = args
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel
    if x["cod"] != "404":
        async with channel.typing():
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_celsiuis = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}", timestamp=ctx.message.created_at, color = 0xeff7e1 )
            embed.add_field(name="Облачность", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Температура(C)", value=f"**{current_temperature_celsiuis}°C**", inline=False)
            embed.add_field(name="Влажность(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Атмосферное давление(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
            await channel.send(embed=embed)
    else:
        em = discord.Embed(title = 'Ошибка!')
        em.add_field(name = 'Причина ошибки:', value = f'Город "{args}" не найден!')
        em.add_field(name = 'Причина ошибки:', value = f'{prefix}weather Москва')
        await ctx.send(embed = em)



@weather.error
async def weather_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите город!', inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}weather Москва', inline=False)
        await ctx.send(embed=b)
#Код погоды списан с https://stackoverflow.com/questions/63486570/how-to-make-a-weather-command-using-discord-py-v1-4-1

#Информация о сервере
@client.command()
async def server_inform(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)
    role_count = len(ctx.guild.roles)
    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(title='Информация о сервере', color = 0xad6c80)
    embed.set_thumbnail(url=icon)
    embed.add_field(name = 'Название сервера:', value = f'{name}', inline=False)
    embed.add_field(name="Основатель сервера:", value=owner, inline=True)
    embed.add_field(name="ID сервера:", value=id, inline=True)
    embed.add_field(name="Регион:", value=region, inline=True)
    embed.add_field(name="Количество пользователей:", value=memberCount, inline=True)
    embed.add_field(name='Уровень верификации:', value=str(ctx.guild.verification_level), inline=False)
    embed.add_field(name='Количество ролей:', value=str(role_count), inline=False)    
    await ctx.send(embed=embed)

#Википедия

@client.command(pass_context=True)
async def wiki(ctx,*, args):
    wikipedia.set_lang('ru')
    bnmm = (wikipedia.summary(args))
    await ctx.send(f'Информация по запросу "{args}": \n {bnmm}')



@wiki.error
async def wiki_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите запрос!', inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}wiki discord', inline=False)
        await ctx.send(embed=b)
#Рандомные изображения
@client.command()
async def anime(ctx):
    response = requests.get('https://some-random-api.ml/animu/hug')
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0xff9900, title='Random Anime')
    embed.set_image(url=json_data['link'])
    embed.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def fox(ctx):
    response = requests.get('https://some-random-api.ml/img/fox')
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0x008000, title='Random Fox')
    embed.set_image(url=json_data['link'])
    embed.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def dog(ctx):
    response = requests.get('https://some-random-api.ml/img/dog')
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0x008000, title='Random Dog')
    embed.set_image(url=json_data['link'])
    embed.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def cat(ctx):
    response = requests.get('https://some-random-api.ml/img/cat')
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0x008000, title='Random Cat')
    embed.set_image(url=json_data['link'])
    embed.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)


@client.command()
async def pikachu(ctx):
    response = requests.get('https://some-random-api.ml/img/pikachu')
    json_data = json.loads(response.text)  # Извлекаем JSON

    embed = discord.Embed(color=0x008000, title='Random Pikachu')  # https://some-random-api.ml/canvas/color
    embed.set_image(url=json_data['link'])
    await ctx.send(embed=embed)
#Парсер StopGame


@client.command()
async def stopgame(ctx):

    def get_html(url, params=None):
        r = requests.get(url, headers = HEADERS, params = params )
        return r
    gay = []
    v = []
    newsw = []
    bb = []
    def get_content(html):

        soup = BeautifulSoup(html, 'html.parser')
        for x in soup.select('.article-summary .caption'):
            newsw.append(x.get_text(strip=True))
    
        articles = soup.find_all('div', class_='caption caption-bold')
        for a in articles:
            bb.append(link+a.find('a')['href'])

        yu = soup.find_all('span', class_ = 'info-item timestamp')
        for c in yu:
            v.append(c.get_text())  
        return v, newsw, bb
    def parse():
        html = get_html(URL)
        print (html)
        get_content (html.text)
    parse()
    


    cvh = discord.Embed(title = 'StopGame', color = 0xFF0000)
    cvh.add_field(name = 'Заголовок:', value = f'1. {newsw[0]} \n 2. {newsw[1]} \n 3. {newsw[2]} \n 4. {newsw[3]} \n 5. {newsw[4]}')
    cvh.add_field(name = 'Ссылка:', value = f'1.{bb[0]} \n 2.{bb[1]} \n 3.{bb[2]} \n 4.{bb[3]} \n 5.{bb[4]}')
    cvh.add_field(name = 'Дата:', value = f'1. {v[0]} \n 2. {v[1]} \n 3. {v[2]} \n 4. {v[3]} \n 5. {v[4]}')
    cvh.set_footer(text=f'Нет, код не списан у Хавуди Хо (Я серъезно)', icon_url = 'https://cdn.discordapp.com/attachments/776796284152971274/793456242201853982/unnamed.jpg')
    await ctx.send(embed = cvh)


@client.command()
async def ping(ctx):
    ping = client.ws.latency  # Получаем пинг клиента для вывода# Изначальное сообщение

    ping_emoji = '🟩🔳🔳🔳🔳'  # Эмоция пинга, если он меньше 100ms

    if ping > 0.10000000000000000:
        ping_emoji = '🟧🟩🔳🔳🔳'  # Эмоция пинга, если он больше 100ms

    if ping > 0.15000000000000000:
        ping_emoji = '🟥🟧🟩🔳🔳'  # Эмоция пинга, если он больше 150ms

    if ping > 0.20000000000000000:
        ping_emoji = '🟥🟥🟧🟩🔳'  # Эмоция пинга, если он больше 200ms

    if ping > 0.25000000000000000:
        ping_emoji = '🟥🟥🟥🟧🟩'  # Эмоция пинга, если он больше 250ms

    if ping > 0.30000000000000000:
        ping_emoji = '🟥🟥🟥🟥🟧'  # Эмоция пинга, если он больше 300ms

    if ping > 0.35000000000000000:
        ping_emoji = '🟥🟥🟥🟥🟥'  # Эмоция пинга, если он больше 350ms

    v = discord.Embed(title='Пинг', color=0xA30DCC)
    v.add_field(name='Понг!', value=f'Пинг бота на данный момент: {(ping * 1000)}{ping_emoji}')
    await ctx.send(embed=v)

@client.command(pass_context=True)
async def shortlink(ctx, nmh: str):
    sdv = pyshorteners.Shortener()
    cccc = sdv.tinyurl.short(nmh)
    embed = discord.Embed(title='Сокращение ссылки')
    embed.add_field(name=f'Ваша ссылка: ', value=f'{cccc}')
    embed.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=embed)


@shortlink.error
async def short(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите ссылку!', inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}shortlink google.com', inline=False)
        await ctx.send(embed=b)


@client.command()
async def hentai (ctx):
    if  ctx.channel.is_nsfw():
        r = ['feet', 'yuri', 'trap', 'futanari', 'hololewd', 'lewdkemo',
            'solog', 'feetg', 'cum', 'erokemo', 'les', 'wallpaper', 'lewdk',
            'ngif', 'tickle', 'lewd', 'feed', 'gecg', 'eroyuri', 'eron',
            'cum_jpg', 'bj', 'nsfw_neko_gif', 'solo', 'kemonomimi', 'nsfw_avatar',
            'gasm', 'poke', 'anal', 'slap', 'hentai', 'avatar', 'erofeet', 'holo',
            'keta', 'blowjob', 'pussy', 'tits', 'holoero', 'lizard', 'pussy_jpg',
            'pwankg', 'classic', 'kuni', 'waifu', 'pat', '8ball', 'kiss', 'femdom',
            'neko', 'spank', 'cuddle', 'erok', 'fox_girl', 'boobs', 'random_hentai_gif',
            'smallboobs', 'hug', 'ero', 'smug', 'goose', 'baka', 'woof'
		    ]
        rnek = nekos.img(random.choice(r))
        emb = discord.Embed(title = 'Дрочить - плохо для зрения!', color = 0xFF1493 )
        emb.set_image(url = rnek)
        await ctx.send(embed = emb)
    else:
        await ctx.send('Это не NSFW канал! Использовать тут команду не получится!')