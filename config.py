import discord
from discord.ext import commands, tasks
api_discord = 'NzU2MTMxMTM3NTE2MjA4MTQ4.X2NX_w.tse6wIiRHkqFEPPf2wB4cFGyMzs'
api_key = 'bb069dc301f0db6922ff48a09d5a0a35'    #Api open weather map
base_url = "http://api.openweathermap.org/data/2.5/weather?"    #Погода
prefix = '/'
client = commands.Bot(command_prefix=f'{prefix}')