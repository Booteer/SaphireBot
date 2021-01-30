import discord
from discord.ext import commands, tasks
api_discord = ''
api_key = ''    #Api open weather map
base_url = "http://api.openweathermap.org/data/2.5/weather?"    #Погода
prefix = '/'
client = commands.Bot(command_prefix=f'{prefix}')   
