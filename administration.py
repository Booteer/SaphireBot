from config import *
import discord
from discord.ext import commands, tasks
from discord.ext.commands import MissingPermissions
import asyncio



#Команда очистки

@client.command()
@commands.has_permissions(view_audit_log=True)
async def clear(ctx, amount: int):
    if amount <= 0:
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Нельзя удалять 0 и меньше сообщений!', inline=False)
        await ctx.send(embed=b)
    if amount >=1000:
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Нельзя удалять 1000 и больше сообщений!', inline=False)
        await ctx.send(embed = b)
    if amount > 0 and amount <1000:
        await ctx.channel.purge(limit=amount)
        a = discord.Embed(title='Очистка чата', color=0xFF1493)
        a.add_field(name='Чат очищен!', value=f'Было удалено {amount} сообщений администратором / модератором {ctx.author.name}')
        a.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=a, delete_after = 10 )


@clear.error
async def clear_error(ctx, error):
    if isinstance(error, MissingPermissions):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='У вас нету нужных прав для управления этой командой! - ```Просматривать журнал аудита```', inline=False)
        await ctx.send(embed=b)
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите количество сообщений для удаления!', inline=False)
        b.add_field(name='Пример использования команды:', value='lu.clear 1')
        await ctx.send(embed=b)


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, args):
    if member == ctx.message.author:
        await ctx.channel.send("Банить самого себя - плохая идея.")
        return
    if ctx.author.top_role == member.top_role:
        await ctx.send('Вы не можете кикнуть того, кто равен вашей роли!')
        return
    if ctx.author.top_role < member.top_role:
        await ctx.send('Вы не можете забанить того, кто выше вас ролью!')
        return
    else:
        lol = discord.Embed(title='Пользователь забанен!', color=0x9400D3)
        lol.add_field(name='Модератор / админ:', value=ctx.message.author.mention, inline=False)
        lol.add_field(name='Нарушитель:', value=member.mention, inline=False)
        lol.add_field(name='Причина:', value=f'{args}', inline=False)
        lol.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
        await ctx.send(embed=lol)
        await member.send(f'Вы забанены по причине "{args}"!')
        await member.ban(reason=args)
    
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='введите пользователя или причину!', inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}ban @user reason', inline=False)
        await ctx.send(embed=b)
    if isinstance(error, MissingPermissions):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='У вас нету нужных прав для управления этой командой! - ```Банить участников```', inline=False)
        await ctx.send(embed=b)

# разбан
@client.command(pass_context=True)
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("Разбан самого себя?")
        return
    await ctx.channel.purge(limit=1)

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban(user)

        await ctx.send(f'Данный пользователь был разбанен администратором {user.mention}.')
        return


@unban.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите пользователя для разбана или введите существующего пользователя!', inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}unban @user', inline=False)
        await ctx.send(embed=b)
    if isinstance(error, commands.MissingPermissions):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='У вас нету нужных прав для управления этой командой! - ```Банить участников```', inline=False)
        await ctx.send(embed=b)

@client.command(pass_context=True)
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, args):
    if member == ctx.message.author:
        await ctx.channel.send("Кикать самого себя - плохая идея.")
        return
    if ctx.author.top_role == member.top_role:
        await ctx.send('Вы не можете кикнуть того, кто равен вашей роли!')
        return
    if ctx.author.top_role < member.top_role:
        await ctx.send('Вы не можете кикнуть того, кто выше вас ролью!')
        return
    else:
        lol = discord.Embed(title='Пользователь кикнут!', color=0x9370DB)
        lol.add_field(name='Модератор / админ:', value=ctx.message.author.mention, inline=False)
        lol.add_field(name='Нарушитель:', value=member.mention, inline=False)
        lol.add_field(name='Причина:', value= f'{args}', inline=False)
        await ctx.send(embed=lol)
        await member.send(f'Вы кикнуты по причние "{args}"')
        await member.kick(reason=args)


@kick.error
async def inform_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите пользователя, котрого хотите кикнуть и причину!',inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}kick @user reason', inline=False)
        await ctx.send(embed=b)
    if isinstance(error, MissingPermissions):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:',value='У вас нету нужных прав для управления этой командой! - ```Выгонять участников```',inline=False)
        await ctx.send(embed=b)












@client.command(pass_context=True)
@commands.has_permissions(manage_roles=True)
async def mute(ctx, member: discord.Member, time:int, *, args):
    mute = discord.utils.get(ctx.message.guild.roles, name='mute')
    if mute != None:
        if member == ctx.message.author:
            await ctx.channel.send("Мутить самого себя - плохая идея.")
            return
        if ctx.author.top_role == member.top_role:
            await ctx.send('Вы не можете замутить того, кто равен вашей роли!')
            return
        if ctx.author.top_role < member.top_role:
            await ctx.send('Вы не можете замутить того, кто выше вас ролью!')
            return
        if time <=0:
            bvb = discord.Embed(title = 'Ошибка!', color = 0xff060e)
            bvb.add_field(name = 'Причина ошибки', value = 'Нельзя мьютить пользователя на 0 и меньше минут!', inline = False)
            await ctx.send(embed = bvb)
        if time >0:
            lol = discord.Embed(title='Пользовтаель отправлен в мут', color=0x708090)
            lol.add_field(name='Модератор / админ:', value=ctx.message.author.mention, inline=False)
            lol.add_field(name='Нарушитель:', value=member.mention, inline=False)
            lol.add_field(name='Причина:', value=f'{args}', inline=False)
            lol.add_field(name='Время:', value=time, inline=False)
            lol.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
            await member.add_roles(mute)
            await ctx.send(embed=lol)
            await member.send(f'Вы отправлены в мут по причине "{args}"!')
            await asyncio.sleep(time * 60)
            await member.remove_roles(mute)
    if mute == None:
        guild = ctx.guild
        perms = discord.Permissions(send_messages=False, read_messages=True)
        await guild.create_role(name="mute", permissions=perms)
        await ctx.send(f'{ctx.message.author.mention}, роль "mute" создана! Пожалуйста, заново напишите команду!')


@mute.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите пользователя для мута, время мута и причину!', inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}mute @user 1 reason', inline=False)
        await ctx.send(embed=b)
    if isinstance(error, MissingPermissions):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:',value='У вас нету нужных прав для управления этой командой! - ```Управлять ролями```', inline=False)
        await ctx.send(embed=b)

@client.command(manage_roles=True)
@commands.has_permissions(manage_roles=True)
async def unmute(ctx, member: discord.Member):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("Анмут самого себя?")
        return
    mute = discord.utils.get(ctx.message.guild.roles, name='mute')
    lolxx = discord.Embed(title='Пользовтаель больше не в муте!', color=0xA52A2A)
    lolxx.add_field(name='Модератор / админ:', value=ctx.message.author.mention, inline=False)
    lolxx.add_field(name='Нарушитель:', value=member.mention, inline=False)
    lolxx.set_footer(text=f'Вызвано: {ctx.message.author}', icon_url=ctx.message.author.avatar_url)
    await ctx.send(embed=lolxx)
    await member.remove_roles(mute)


@unmute.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='Введите пользователя для анмута!', inline=False)
        b.add_field(name='Пример использования команды:', value=f'{prefix}unmute @user', inline=False)
        await ctx.send(embed=b)
    if isinstance(error, MissingPermissions):
        b = discord.Embed(title='Ошибка!', color=0xff060e)
        b.add_field(name='Причина ошибки:', value='У вас нету нужных прав для управления этой командой! - ```Управлять ролями```', inline=False)
        await ctx.send(embed=b)