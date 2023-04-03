import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6109845361:AAH4FROLCWm__f74n9CP75GtjwCCpVuTqh4")

API_ID = int(os.environ.get("API_ID", "18302370"))

API_HASH = os.environ.get("API_HASH", "03c2cced4dea9b1e96dce87558dd2381")

STRING = os.environ.get("STRING", "BQDimrUATUjWtBsSFIw6tbnA5MxvWaSDFbhSqB4wtOP89QBUjH21KgvUbUPKDMbo_0qgoaEECfPd2zE6baieoEPI-leYnVRUT8ZYTH-WG8hp5z3qlBaKbPftN8PtQoLAskeT7QyPqe50IzkDAdC7XocC7DqbQlDzprJYwtrH4A1u7AIgDmuMg6XvJRa8bmie-IyqcEJM7PPGe5cdSsOPnQ9mSEZInY2hK7briWLI_WReeBI4JCsu3CqQKRZAu8iIr3YFVI1L9BZQD3MXzELrMzkBtN-vPHsyvypThWxKw9qL3970Rhdtokrje7FFD8r0VuvnaVba9PiRPK1DwC8S_FQs4f9-wQAAAAFSdMRBAA")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
