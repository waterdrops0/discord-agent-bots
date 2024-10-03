import discord
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the token from the environment variable
DISCORD_TOKEN = os.getenv('DISCORD_PRENOTES_TOKEN')

# Set the n8n webhook URL
N8N_ENDPOINT = "https://waterdrops.app.n8n.cloud/webhook-test/pre-notes"

# Set up intents
intents = discord.Intents.default()
intents.message_content = True  # Allows the bot to read message content

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')

    async def on_message(self, message):
        if message.author == self.user:
            return

        # Respond to the !pre-notes command
        if message.content.startswith('!pre-notes'):
            try:
                # Call the n8n webhook URL
                response = requests.get(N8N_ENDPOINT)
                if response.status_code == 200:
                    await message.channel.send(f"Pre-Notes: {response.text}")
                else:
                    await message.channel.send(f"Error: Unable to fetch pre-notes. Status code: {response.status_code}")
            except Exception as e:
                await message.channel.send(f"Error: {e}")

# Run the bot with intents
client = MyClient(intents=intents)
client.run(DISCORD_TOKEN)
