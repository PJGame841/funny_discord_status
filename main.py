import discord
import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
	print("Connected", flush=True)
	activity = discord.CustomActivity(name="with the API", emoji=client.get_emoji(":robot:"))
	print(activity, flush=True)
	await client.change_presence(activity=activity, afk=False)
	
@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		print("[+]: Status Changer Loaded")
		altern = False
		headers = {
			'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
			'Content-Type': 'application/json',
			'Authorization': os.getenv('DISCORDTOKEN'),
    }
		request = requests.Session()
		while True:
			setting = {
					'status': "online",
					"custom_status": {"text": "-======-" if altern else "-______-"},
			}
			res = request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
			print(res.headers)
			print(res.json())
			altern = not altern
			time.sleep(3)
		
client.run(os.getenv('DISCORDTOKEN'), bot=False)