import discord, random
from keep_alive import keep_alive
from discord.ext import commands
from discord.ext.tasks import loop
import os
activity = discord.Game(name="suk on deez nuts haahha")
#Streaming -> activity = discord.Streaming(name="!help", url="twitch_url_here")
#Listening -> activity = discord.Activity(type=discord.ActivityType.listening, name="!help")
#Watching -> activity = discord.Activity(type=discord.ActivityType.watching, name="!help")
bot = commands.Bot(command_prefix='!',
                   activity=activity,
                   status=discord.Status.online)
bot.remove_command('help')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(name='kill')
async def ping(ctx, user: discord.User):
    killran = [
        f"<@{user.id}> is gay hahahaha",
        f" <@{ctx.author.id}> called you sus! :rofl:"
    ]
    killran2 = [
        "https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/99df7fe6-5010-43ea-a4e2-0c6f99b44a53/ddrud5w-088068d5-7e04-49a2-91ce-ecbd6e547675.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzk5ZGY3ZmU2LTUwMTAtNDNlYS1hNGUyLTBjNmY5OWI0NGE1M1wvZGRydWQ1dy0wODgwNjhkNS03ZTA0LTQ5YTItOTFjZS1lY2JkNmU1NDc2NzUucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.wyq2ETa6P7QjtKBknQ14DgiQWOw8JKNwDLkMm70EICA\n",
        "https://img.ifunny.co/images/d7e3ee1ec65cfb2e55b141d013feb7102d481014caab9626c17329054969694f_1.jpg"
    ]
    randomnum = random.randint(0, len(killran) - 1)

    await ctx.send(killran[randomnum])
    await ctx.send(killran2[randomnum])


@bot.command(name='mute')
async def mute(ctx, user: discord.User):
    await ctx.send("shut up bozo")
    await user.add_roles(discord.utils.get(user.guild.roles,
                                           name='muted'))  #add the role


@bot.event
async def on_message(ctx):
    author = ctx.author.id
    user_msg = ctx.content
    user = ctx.author.id
    usern = ctx.author.name
    if ctx.author != bot.user:
        if "keyword" in user_msg:
            await ctx.channel.send(
                f"<@{user}> basicaly what you want it to say"
            )  #add ,delete_after=5 if you want it to be deleted
        elif "keyword2" in user_msg:
            await ctx.channel.send(
                f"<@{user}> basicaly what you want it to say2"
            )  #add ,delete_after=5 if you want it to be deleted
    await bot.process_commands(ctx)


keep_alive()
bot.run(os.environ['TOKEN'])
#how to get a token
#https://discord.com/developers/applications
#new application
#Bot
#Create bot
#Name it and all
#copy token
