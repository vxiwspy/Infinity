import asyncio, time, aiolimiter, random, string, os, requests

from typing import Callable
from colored import fg
from colorama import Fore
from aiohttp import ClientSession
from datetime import datetime

import discord
from discord.ext import commands

#for designing, bad code

now = datetime.now()
t = now.strftime("%H:%M:%S")
gray = fg(59)
magenta = fg(93)
blue = fg(57)
w = Fore.WHITE

########################

vxiw = commands.Bot(command_prefix="krizz", intents=discord.Intents.all())
token = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Token {blue}>> {Fore.WHITE}")

class Infinity():

    def __init__(self, token, limit=50):

        self.__VERSION__ = "1.1.0"
        self.__AUTHOR__  = "@vxiws/Phantom111.py on cord"

        self.token   =  token
        self.limiter =  aiolimiter.AsyncLimiter(limit, 1)

        self.ng = ""

    def get_headers(self: str) -> dict:
        """ returns headers of the token """

        return {"authorization": f"Bot {self.token}"}
    
    """
    def get_cookies(self, token = self.token) -> Callable:
        session  = requests.Session()
        response = session.get("https://discord.com/api/v9/users/@me", headers={"authorization": token})

        return session.cookies.get_dict()
    """

    async def print_banner(self):
        banner = f"""
        
                                 ______           ______  __          __   __              
                                |      \         /      \|  \        |  \ |  \             
                                \▓▓▓▓▓▓_______ |  ▓▓▓▓▓▓\ ▓▓_______  \▓▓_| ▓▓_   __    __ 
                                 | ▓▓ |       \| ▓▓_  \▓▓  \       \|  \   ▓▓ \ |  \  |  
                                 | ▓▓ | ▓▓▓▓▓▓▓\ ▓▓ \   | ▓▓ ▓▓▓▓▓▓▓\ ▓▓\▓▓▓▓▓▓ | ▓▓  | ▓▓
                                 | ▓▓ | ▓▓  | ▓▓ ▓▓▓▓   | ▓▓ ▓▓  | ▓▓ ▓▓ | ▓▓ __| ▓▓  | ▓▓
                                _| ▓▓_| ▓▓  | ▓▓ ▓▓     | ▓▓ ▓▓  | ▓▓ ▓▓ | ▓▓|  \ ▓▓__/ ▓▓
                               |   ▓▓ \ ▓▓  | ▓▓ ▓▓     | ▓▓ ▓▓  | ▓▓ ▓▓  \▓▓  ▓▓\▓▓    ▓▓
                                \▓▓▓▓▓▓\▓▓   \▓▓\▓▓      \▓▓\▓▓   \▓▓\▓▓   \▓▓▓▓ _\▓▓▓▓▓▓▓
                                                                                |  \__| ▓▓
                                                                                 \▓▓    ▓▓
                                                                                   \▓▓▓▓▓▓
                                                                        """.replace("_", f"{Fore.RESET}_{Fore.RESET}").replace(f'|', f"{Fore.RESET}|{Fore.RESET}").replace("▓", f"{magenta}▓{Fore.RESET}")
        print(f"{banner}\n\n")
        os.system("clear")


    async def menu(self):
        os.system("clear")
        banner = f"""
        
                                 ______           ______  __          __   __              
                                |      \         /      \|  \        |  \ |  \             
                                 \▓▓▓▓▓▓_______ |  ▓▓▓▓▓▓\ ▓▓_______  \▓▓_| ▓▓_   __    __ 
                                 | ▓▓ |       \| ▓▓_  \▓▓  \       \|  \   ▓▓ \ |  \  |  
                                 | ▓▓ | ▓▓▓▓▓▓▓\ ▓▓ \   | ▓▓ ▓▓▓▓▓▓▓\ ▓▓\▓▓▓▓▓▓ | ▓▓  | ▓▓
                                 | ▓▓ | ▓▓  | ▓▓ ▓▓▓▓   | ▓▓ ▓▓  | ▓▓ ▓▓ | ▓▓ __| ▓▓  | ▓▓
                                _| ▓▓_| ▓▓  | ▓▓ ▓▓     | ▓▓ ▓▓  | ▓▓ ▓▓ | ▓▓|  \ ▓▓__/ ▓▓
                               |   ▓▓ \ ▓▓  | ▓▓ ▓▓     | ▓▓ ▓▓  | ▓▓ ▓▓  \▓▓  ▓▓\▓▓    ▓▓
                                \▓▓▓▓▓▓\▓▓   \▓▓\▓▓      \▓▓\▓▓   \▓▓\▓▓   \▓▓▓▓ _\▓▓▓▓▓▓▓
                                                                                |  \__| ▓▓
                                                    {magenta}@vxiws/phantom{w} On Cord       \▓▓    ▓▓
                                                                                  \▓▓▓▓▓▓


                                {magenta}01{w}: Scrape Server       {magenta}05{w}: Make Channels     {magenta}00{w}: Coming Soon
                                {magenta}02{w}: Ban Member/IDs      {magenta}06{w}: Delete Roles      {magenta}00{w}: Coming Soon
                                {magenta}03{w}: Kick Members        {magenta}07{w}: Make Roles        {magenta}00{w}: Coming Soon
                                {magenta}04{w}: Delete Channels     {magenta}08{w}: Spam Messages     {magenta}00{w}: Coming Soon


                                                                       {w}""".replace("_", f"{Fore.RESET}_{Fore.RESET}").replace(f'|', f"{Fore.RESET}|{Fore.RESET}").replace("▓", f"{magenta}▓{Fore.RESET}")
        ch = input(f"""
{banner}

{magenta}[{blue}Infinity {w}v1.11{magenta}]{w} Choice {blue}~$ {Fore.WHITE}""")

        if ch in ["01", "1"]:

            guild = input(f"\n{gray}{t}{Fore.WHITE}   {Fore.WHITE}Guild ID {blue}>> {Fore.WHITE}")
            await self.scrape_server(guild)

        elif ch in ["02", "2"]:
            await self.ban_members()
        elif ch in ["03", "3"]:
            await self.kick_members()
        elif ch in ["04", "4"]:
            await self.delete_channels()
        elif ch in ["05", "5"]:
            await self.make_channels()
        elif ch in ["06", "6"]:
            await self.delete_roles()
        elif ch in ["07", "7"]:
            await self.make_roles()
        elif ch in ["08", "8"]:
            await self.spam_messages()


    async def scrape_server(self, guild_id):
        await self.print_banner()

        @vxiw.event
        async def on_ready():

            guild = vxiw.get_guild(int(guild_id))
            self.ng = guild

            with open("scraped/members.txt", "w") as membs:
                for m in guild.members:
                    membs.write(f"{m.id}\n")
            
            with open("scraped/channels.txt", "w") as chs:
                for c in guild.channels:
                    chs.write(f"{c.id}\n")
            
            with open("scraped/roles.txt", "w") as rs:
                for r in guild.roles:
                    rs.write(f"{r.id}\n")

            print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Scraped Members{blue}    >> {Fore.WHITE}{len(guild.members)}")
            print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Scraped Channels{blue}   >> {Fore.WHITE}{len(guild.channels)}")
            print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Scraped Roles{blue}      >> {Fore.WHITE}{len(guild.roles)}")
            time.sleep(5)
            await self.menu()
            

    async def ban(self, guild, member):
        async with self.limiter:
            async with ClientSession(headers=self.get_headers()) as session:
                response = await session.put(f"https://discord.com/api/v9/guilds/{guild}/bans/{member}")
                f = member.replace("\n", "")
                if response.status in [200,201,204]:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Successfully Banned{blue}   >> {Fore.WHITE}{f}")

                elif response.status == 429:
                    json = await response.json()
                    await asyncio.sleep(json['retry_after'])
                    await self.ban(guild, member)

                else:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Unsuccessfull Ban{blue}     >> {Fore.WHITE}{f}")
    
    async def ban_members(self):
        ids   = input(f"\n{gray}{t}{Fore.WHITE}   {Fore.WHITE}Ban IDs? (y/n) {blue}>> {Fore.WHITE}")
        guild = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Guild ID       {blue}>> {Fore.WHITE}")

        await self.print_banner()

        if ids == "y":
            with open("scraped/ids.txt", "r") as ids_:
                ids__ = ids_.readlines()
            tasks = [asyncio.create_task(self.ban(guild, id)) for id in ids__]
            await asyncio.wait(tasks)

            time.sleep(5)
            await self.menu()

        else:
            with open("scraped/members.txt", "r") as ids_:
                ids__ = ids_.readlines()
            tasks = [asyncio.create_task(self.ban(guild, id)) for id in ids__]
            await asyncio.wait(tasks)

            time.sleep(5)
            await self.menu()


    async def kick(self, guild, member):
        async with self.limiter:
            async with ClientSession(headers=self.get_headers()) as session:
                response = await session.delete(f"https://discord.com/api/v9/guilds/{guild}/members/{member}")
                f = member.replace("\n", "")
                if response.status in [200,201,204]:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Successfully Kicked{blue}   >> {Fore.WHITE}{f}")

                elif response.status == 429:
                    json = await response.json()
                    await asyncio.sleep(json['retry_after'])
                    await self.kick(guild, member)

                else:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Unsuccessfull Kick{blue}    >> {Fore.WHITE}{f}")

    async def kick_members(self):
        guild = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Guild ID   {blue}>> {Fore.WHITE}")

        await self.print_banner()

        with open("scraped/members.txt", "r") as ids_:
            ids__ = ids_.readlines()
            tasks = [asyncio.create_task(self.kick(guild, id)) for id in ids__]
            await asyncio.wait(tasks)

            time.sleep(5)
            await self.menu()

    async def delch(self, ch):
        async with self.limiter:
            async with ClientSession(headers=self.get_headers()) as session:
                response = await session.delete(f"https://discord.com/api/v9/channels/{ch}")
                f = ch.replace("\n", "")
                if response.status in [200,201,204]:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Successfully Deleted{blue}   >> {Fore.WHITE}{f}")

                elif response.status == 429:
                    json = await response.json()
                    await asyncio.sleep(json['retry_after'])
                    await self.delch(ch)

                else:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Unsuccessfull Channel{blue}  >> {Fore.WHITE}{f}")

    async def delete_channels(self):
        await self.print_banner()


        with open("scraped/channels.txt", "r") as ids_:
                
            ids__ = ids_.readlines()
            tasks = [asyncio.create_task(self.delch(id)) for id in ids__]
            await asyncio.wait(tasks)

            time.sleep(5)
            await self.menu()

    async def makech(self, guild, name):
        async with self.limiter:
            async with ClientSession(headers=self.get_headers()) as session:
                response = await session.post(f"https://discord.com/api/v9/guilds/{guild}/channels", json={"name": name, "type": 0})
                if response.status in [200,201,204]:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Successfully Created{blue}   >> {Fore.WHITE}{name}")

                elif response.status == 429:
                    json = await response.json()
                    await asyncio.sleep(json['retry_after'])
                    await self.makech(guild, name)

                else:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Unsuccessfull Channel{blue}   >> {Fore.WHITE}{await response.json()}")

    async def make_channels(self):
        guild = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Guild ID   {blue}>> {Fore.WHITE}")
        times = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Times      {blue}>> {Fore.WHITE}")
        name  = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Name       {blue}>> {Fore.WHITE}")

        await self.print_banner()

    
        tasks = [asyncio.create_task(self.makech(guild, name)) for _ in range(int(times))]
        await asyncio.wait(tasks)

        time.sleep(5)
        await self.menu()

    async def delrl(self, role):
        async with self.limiter:
            async with ClientSession(headers=self.get_headers()) as session:
                response = await session.delete(f"https://discord.com/api/v9/roles/{role}")
                f = role.replace("\n", "")
                if response.status in [200,201,204]:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Successfully Deleted{blue}   >> {Fore.WHITE}{f}")

                elif response.status == 429:
                    json = await response.json()
                    await asyncio.sleep(json['retry_after'])
                    await self.delrl(role)

                else:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Unsuccessfull Role {blue}    >> {Fore.WHITE}{f}")

    async def delete_roles(self):
        await self.print_banner()


        with open("scraped/roles.txt", "r") as ids_:
                
            ids__ = ids_.readlines()
            tasks = [asyncio.create_task(self.delrl(id)) for id in ids__]
            await asyncio.wait(tasks)

            time.sleep(5)
            await self.menu()

    async def makerl(self, guild, name):
        async with self.limiter:
            async with ClientSession(headers=self.get_headers()) as session:
                response = await session.post(f"https://discord.com/api/v9/guilds/{guild}/roles", json={"name": name, "type": 0})
                if response.status in [200,201,204]:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Successfully Created{blue}   >> {Fore.WHITE}{name}")

                elif response.status == 429:
                    json = await response.json()
                    await asyncio.sleep(json['retry_after'])
                    await self.makerl(guild, name)

                else:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Unsuccessfull Role{blue}     >> {Fore.WHITE}{await response.json()}")


    async def make_roles(self):
        guild = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Guild ID   {blue}>> {Fore.WHITE}")
        times = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Times      {blue}>> {Fore.WHITE}")
        name  = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Name       {blue}>> {Fore.WHITE}")

        await self.print_banner()

    
        tasks = [asyncio.create_task(self.makerl(guild, name)) for _ in range(int(times))]
        await asyncio.wait(tasks)

        time.sleep(5)
        await self.menu()

    async def spam_ch(self, ch, message):
        async with self.limiter:
            async with ClientSession(headers=self.get_headers()) as session:
                response = await session.post(f"https://discord.com/api/v9/channels/{ch}/messages", json={"content": message})

                cha = ch.replace("\n", "")
                if response.status in [200,201,204]:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Successfully Spammed{blue}   >> {Fore.WHITE}{cha}")

                elif response.status == 429:
                    json = await response.json()
                    await asyncio.sleep(json['retry_after'])
                    await self.spam_ch(ch, message)

                else:
                    print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Unsuccessfull Spam{blue}     >> {Fore.WHITE}{await response.json()}")

    async def r_c(self, g):

        guild = self.ng
        with open("scraped/channels.txt", "w") as chs:
            for c in guild.channels:
                chs.write(f"{c.id}\n")
            

    async def spam_ex(self, times, channel, message):
        tasks = [asyncio.create_task(self.spam_ch(channel, message)) for _ in range(int(times))]
        await asyncio.wait(tasks)


    async def spam_messages(self):
        guild    = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Guild ID   {blue}>> {Fore.WHITE}")
        message  = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Message    {blue}>> {Fore.WHITE}")
        times    = input(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Times      {blue}>> {Fore.WHITE}")

        await self.r_c(guild)

        with open("scraped/channels.txt", "r") as chs:
            channels = chs.readlines()

        await self.print_banner()


        tasks = [asyncio.create_task(self.spam_ex(times, channel, message)) for channel in channels]
        await asyncio.wait(tasks)

        time.sleep(3)
        await self.menu()
        



    """
    async def info(self):
        async with ClientSession(headers=self.get_headers()) as session:
            response = await session.get("https://discord.com/api/v9/users/@me")

            if response.status == 200:
                return await response.json()
            else:
                return
    """

    """
    async def token_info(self):
        inf = await self.info()
        await self.print_banner()

        username = inf['username']
        phone    = inf['phone']
        email    = inf['email']
        display  = inf['global_name']
        bio      = inf['bio']
        avatar   = inf['avatar']

        print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Display{blue}   >> {Fore.WHITE}{display}")
        print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Username{blue}  >> {Fore.WHITE}{username}")
        print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Email{blue}     >> {Fore.WHITE}{email}")
        print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Phone{blue}     >> {Fore.WHITE}{phone}")
        print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Bio{blue}       >> {Fore.WHITE}{bio}")
        print(f"{gray}{t}{Fore.WHITE}   {Fore.WHITE}Avatar{blue}    >> {Fore.WHITE}{avatar}")
        time.sleep(5)
        await self.menu()
    """

infinity = Infinity(token)

os.system("clear")
asyncio.run(infinity.menu())

vxiw.run(token)
