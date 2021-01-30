import discord
from discord.ext import commands, tasks
from config import *
import random

hugs = ['https://cdn.discordapp.com/attachments/776796284152971274/791622485547679754/anime-hug-83.gif', 'https://cdn.discordapp.com/attachments/776796284152971274/791624440407785492/anime-hug-20.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291988742733824/anime-hug-25.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291987619053618/anime-hug-21.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291985207590932/anime-hug-17.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291984838098974/anime-hug-30.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291950734868531/anime-hug-19.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291944073658408/anime-hug-15.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291943546093578/anime-hug-6.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291941813321788/anime-hug-12.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291868123070474/anime-hug-27.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291862176595968/anime-hug-63.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291861600796672/anime-hug-14.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291861899640832/anime-hug-52.gif', 'https://cdn.discordapp.com/attachments/761579957804597309/796291855347220510/anime-hug-86.gif']   
kisses = ['https://discord.com/channels/783689888892715057/783689888892715060/796051842244280330', 'https://cdn.discordapp.com/attachments/783689888892715060/796051551650971698/anime-kissin-5.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796051704050614282/anime-kissin-8.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796051761889804318/anime-kissin-10.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796051841875836979/anime-kissin-13.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796052118104309831/anime-kiss-29.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796052185028362270/anime-kiss-36.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796052302804549632/anime-kiss-25.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796052362304159775/anime-kiss-23.gif']
teas = ['https://cdn.discordapp.com/attachments/783689888892715060/796064098046705694/GQbY.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796064099200270366/UqPr.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796064100836835399/DWbF.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796064102555451402/6ezZ.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796064105295118396/DWbB.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796064107358715922/K1nG.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796065106693193828/tea-72.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796065107138314280/tea-35.gif']
slides = ['https://cdn.discordapp.com/attachments/770263301698486274/796073531443380244/7KGp.gif', 'https://cdn.discordapp.com/attachments/770263301698486274/796073531443380244/7KGp.gif','https://cdn.discordapp.com/attachments/770263301698486274/796073567463931934/ef8fab9eb8cc1fca9451815b9be26f774640e276r1-436-245_hq.gif', 'https://cdn.discordapp.com/attachments/770263301698486274/796073593003704370/headpat_3903cc_6500559.gif', 'https://cdn.discordapp.com/attachments/770263301698486274/796073614104592419/1tZL.gif', 'https://cdn.discordapp.com/attachments/770263301698486274/796073626704936980/a003123a85cc7c75671ae443a6da1864ff55c878_hq.gif']
ooo = ['https://cdn.discordapp.com/attachments/783689888892715060/796087088931274782/JTSO.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796087066311655454/OWba.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796087044526178324/Rd88.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796087024544120852/FK0b.gif', 'https://cdn.discordapp.com/attachments/783689888892715060/796087000775655434/TQxl.gif']
@client.command()
async def hug (ctx, member:discord.Member):
    if member == None or member == ctx.message.author:
        slaa = (random.choice(hugs))
        bs = discord.Embed(title = 'Обнимашки', color = 0xFFA07A)
        bs.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} обнял самого себя!')
        bs.set_image(url = slaa)
        await ctx.send (embed = bs)
    if member != ctx.message.author:
        slaaa = (random.choice(hugs))
        b = discord.Embed (title = 'Обнимашки!', color = 0xFFA07A)
        b.add_field(name= ':3', value= f'Пользоватлеь {ctx.message.author} обнял {member.mention}.')
        b.set_image(url = slaaa)
        await ctx.send(embed = b)
@hug.error
async def hugerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Обнимашки!', color = 0xFFA07A)
        b.add_field(name = ':3', value = f'Ура, пользователь {ctx.message.author} никого не обнял!')
        b.set_image(url = 'https://cdn.discordapp.com/attachments/783689888892715060/795735858610176010/no.gif')
        await ctx.send (embed = b)

@client.command()
async def kiss(ctx, member:discord.Member):
    if member == None or member == ctx.message.author:
        ve = (random.choice(kisses))
        bs = discord.Embed(title = 'Поцелуй!', color = 0xFF0000)
        bs.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} поцеловал самого себя!')
        bs.set_image(url = ve)
        await ctx.send (embed = bs)
    if member != ctx.message.author:
        ves = (random.choice(kisses))
        b = discord.Embed (title = 'Поцелуй!',color = 0xFF0000)
        b.add_field(name= ':3', value= f'Пользоватлеь {ctx.message.author} поцеловал {member.mention}.')
        b.set_image(url = ves)
        await ctx.send(embed = b)
@kiss.error
async def hugerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Поцелуй!', color = 0xFF0000)
        b.add_field(name = ':3', value = f'Ура, пользователь {ctx.message.author} никого не поцеловал!')
        b.set_image(url = 'https://cdn.discordapp.com/attachments/783689888892715060/796054164773404682/C1la.gif')
        await ctx.send (embed = b)


@client.command()
async def tea (ctx, member:discord.Member):
    if member == None or member == ctx.message.author:
        nb = (random.choice(teas))
        nn = discord.Embed(title = 'Попьём чаёчку!', color = 0xD2691E)
        nn.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} попил чай наедине с собой.')
        nn.set_image(url = nb)
        await ctx.send(embed = nn)
    if member != ctx.message.author:
        mnj = (random.choice(teas))
        oo = discord.Embed(title = 'Попьём чаёчку!', color = 0xD2691E)
        oo.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} попил чай с {member.mention}.')
        oo.set_image(url = mnj)
        await ctx.send (embed = oo)
@tea.error
async def hugerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        mnjn = (random.choice(teas))
        b = discord.Embed(title='Попьём чаёчку!', color = 0xD2691E )
        b.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} попил чай наедине с собой.')
        b.set_image(url = mnjn)
        await ctx.send (embed = b)



@client.command()
async def pat (ctx, member:discord.Member):
    if member == None or member == ctx.message.author:
        nb = (random.choice(slides))
        nn = discord.Embed(title = 'Погладить!', color = 0xADFF2F)
        nn.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} погладил самого себя.')
        nn.set_image(url = nb)
        await ctx.send(embed = nn)
    if member != ctx.message.author:
        mnj = (random.choice(slides))
        oo = discord.Embed(title = 'Погладить!', color = 0xADFF2F)
        oo.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} погладил {member.mention}.')
        oo.set_image(url = mnj)
        await ctx.send (embed = oo)
@pat.error
async def hugerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Погладить!', color = 0xADFF2F)
        b.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} никого не погладил.')
        b.set_image(url = 'https://cdn.discordapp.com/attachments/783689888892715060/796076529708826644/unnamed.gif')
        await ctx.send (embed = b)

@client.command()
async def poke(ctx, member:discord.Member):
    if member == None or member == ctx.message.author:
        nb = (random.choice(ooo))
        nn = discord.Embed(title = 'Тык!', color = 0x8A2BE2)
        nn.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} тыкнул.')
        nn.set_image(url = nb)
        await ctx.send(embed = nn)
    if member != ctx.message.author:
        mnj = (random.choice(ooo))
        oo = discord.Embed(title = 'Тык!', color = 0x8A2BE2)
        oo.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} тыкнул {member.mention}.')
        oo.set_image(url = mnj)
        await ctx.send (embed = oo)

@poke.error
async def hugerror(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Тык!', color = 0x8A2BE2)
        b.add_field(name = ':3', value = f'Пользоватлеь {ctx.message.author} никого не тыкнул.')
        b.set_image(url = 'https://cdn.discordapp.com/attachments/783689888892715060/796088667764031548/3e8f7c79481913c4d84222e2189d28b3f39a00e5_hq.gif')
        await ctx.send (embed = b)
