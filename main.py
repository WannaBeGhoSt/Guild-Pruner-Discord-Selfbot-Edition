import os
os.system("pip install discord.py==1.7.3")
os.system('sleep 2 && clear >/dev/null 2>&1 &' if os.name == 'posix' else 'timeout /t 2 >nul 2>&1 && cls')

import sys
import discord
import asyncio
from discord.ext import commands

ghosty = commands.Bot(command_prefix="ghostyjija", case_insensitive=False, self_bot=True, intents=discord.Intents.all())


def haha(text):
    gradient_length = len(text)
    gradient = [
        f"\033[38;2;0;0;{255 - int((i / gradient_length) * 255)}m"  
        for i in range(gradient_length)
    ]

    output = ""
    for char, color_code in zip(text, gradient):
        output += color_code + char

    
    output += "\033[0m"
    return output

text = """
                                    GHOSTY                                           
ooooooooo.   ooooooooo.   ooooo     ooo ooooo      ooo oooooooooooo ooooooooo.   
`888   `Y88. `888   `Y88. `888'     `8' `888b.     `8' `888'     `8 `888   `Y88. 
 888   .d88'  888   .d88'  888       8   8 `88b.    8   888          888   .d88' 
 888ooo88P'   888ooo88P'   888       8   8   `88b.  8   888oooo8     888ooo88P'  
 888          888`88b.     888       8   8     `88b.8   888    "     888`88b.    
 888          888  `88b.   `88.    .8'   8       `888   888       o  888  `88b.  
o888o        o888o  o888o    `YbodP'    o8o        `8  o888ooooood8 o888o  o888o 
                                Selfbot Edition                                                               
                                                                                 
"""

print(haha(text))


@ghosty.event
async def on_ready():
    print(f"{ghosty.user} Connected")
    await asyncio.sleep(2.5)
    response = input(f"Are you sure you want to prune server {server_id} (Y/N): ")
    if response.lower() in ('y', 'yes'):
        await ghosty_prune()
    elif response.lower() in ('n', 'no'):
        print("Exiting.")
        exit()
    else:
        print("Invalid response. Exiting.")
        exit() 

# CONFIGURE THIS
#######################################################
wall_role = False     # server has wall role yes or no

wall_role_id = 0      # if no wall role then 0

server_id = 1204457412958879795   # server id to prune
#######################################################


async def ghosty_prune():
    guild = ghosty.get_guild(server_id)
    if not guild:
        print("Server not found.")
        return
    
    if not guild.me.guild_permissions.administrator and not guild.me.guild_permissions.kick_members:
        print("Insufficient permissions to prune members.")
        return

    ghosty_roles = [role for role in guild.roles if len(role.members) != 0];reason = "GhoSty Was Here"
    ghosty_pruned = await guild.prune_members(days=1, roles=ghosty_roles, reason=reason)
    print("Pruned:", ghosty_pruned)

async def on_ready():
    print(f"{ghosty.user} Connected")
    await asyncio.sleep(2.5)
    response = input(f"Are you sure you want to prune server {server_id} (Y/N): ")
    if response.lower() in ('y', 'yes'):
        await ghosty_prune()
    elif response.lower() in ('n', 'no'):
        print("Exiting.")
        raise SystemExit(0)  
    else:
        print("Invalid response. Exiting.")
        raise SystemExit(1)

# ACCOUNT TOKEN
ghosty.run("", bot=False)