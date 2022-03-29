import discord
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

class DiscordClient(discord.Client):
	def __init__(self, *args, **kwargs):
		discord.Client.__init__(self, **kwargs)

	async def on_ready(self):
		# user = await self.fetch_user("264026681931464704")
		# now = datetime.datetime.now()
		# channel = await user.create_dm()
		# await channel.send('Api Success! at ' + str(now))
		# print('Success!')
		# await self.close()

		print("Connected", flush=True)
		activity = discord.CustomActivity(name="with the API", emoji=self.get_emoji(":robot:"))
		print(activity, flush=True)
		await self.change_presence(status=discord.Status.idle, activity=activity)

# Main
if __name__ == '__main__':
	dc = DiscordClient()
	dc.run(os.getenv('DISCORDTOKEN'), bot=False)