import discord
import os
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
		# activity = discord.CustomActivity(name="with the API", emoji=client.get_emoji(":robot:"))
		activity = discord.Streaming(name="with the API", url="https://twitch.tv/robot")
		print(activity, flush=True)
		await client.change_presence(activity=activity, afk=False)
		
client.run(os.getenv('DISCORDTOKEN'), bot=False)