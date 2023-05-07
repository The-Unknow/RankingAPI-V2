from fastapi import FastAPI
import os
from roblox import Client
from dotenv import load_dotenv
import asyncio
load_dotenv()

from roblox.utilities.exceptions import InternalServerError
from roblox import InternalServerError


RobloxCookie = os.getenv("COOKIE")
APIKEY = os.getenv("API_KEY")


client = Client(RobloxCookie)

app = FastAPI()

@app.get("/group/shout/")
async def read_items(key: str, message: str):
    if key == APIKEY:
     group = await client.get_group(15328728)
     await group.update_shout(message)
     return ("Successfully Shouted!")
    else:
        return "Incorrect key"

@app.get("/group/promote/")
async def read_items(key: str, username: str):
    if key == APIKEY:
     group = await client.get_group(15328728)
     user_name = await group.get_member_by_username(username)
     membertorank = user_name.id
     await client.set_role(membertorank, +1)
     return ("The user was promoted!")
    else:
        return "Incorrect key"

@app.get("/group/demote/")
async def read_items(user_name: str, key: str, groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     usernameinsystem = await client.get_user_by_username(user_name)
     user_id = usernameinsystem.id
     membertorank =  await group.get_member_by_id(user_id)
     await membertorank.demote()
     return ("The user was demoted!")
    else:
        return "Incorrect key"

@app.get("/group/rank/")
async def read_items(user_name: str, key: str, groupid: int, role_number: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     target = await group.get_member_by_username(user_name)
     await target.setrole(role_number)
     return ("The user had their ranked changed")
    else:
        return "Incorrect key"

@app.get("/group/members/")
async def read_items(key: str, groupid: int):
    if key == APIKEY:
     group = await client.get_group(groupid)
     return (group.member_count)
    else:
        return "Incorrect key"

