import os 
import discord
import asyncio  # For managing async code
from gradio_client import Client  # Import Gradio Client

# Discord bot token
TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# Gradio API setup
GRADIO_API_URL = "waterdrops0/mistral-nouns400"  # Only the space name is required here

# Discord client setup
# Setting up intents
intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent

# Create a Discord client
client = discord.Client(intents=intents)

# Function to query Hugging Face space using the Gradio client
async def query_huggingface_space(prompt):
    try:
        # Initialize the Gradio client
        gr_client = Client(GRADIO_API_URL)

        # Log the prompt sent to the model
        print(f"Sending prompt to Hugging Face: {prompt}")

        # Make the API call using the Gradio client
        result = gr_client.predict(
            prompt=prompt,              # The prompt passed from the user
            max_length=50,              # Max length of generated text
            temperature=0.7,            # Control randomness of output
            repetition_penalty=1.2,     # Penalize repetition
            api_name="/predict"         # Gradio API endpoint
        )

        # Log the result from the Gradio model
        print(f"Response from model: {result}")
        return result  # Return the model's response
    
    except Exception as e:
        print(f"Error querying Hugging Face: {e}")
        return f"Error: {e}"

# Event triggered when the bot is ready
@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

# Event triggered when a message is received
@client.event
async def on_message(message):
    # Log when a message is received along with its content
    print(f"Message received: '{message.content}' from {message.author}")

    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Listen for the command starting with !ask
    if message.content.startswith('!ask'):
        prompt = message.content[len('!ask'):].strip()  # Remove the command and get the prompt

        # Log the prompt that will be sent to Hugging Face
        print(f"Processing command with prompt: '{prompt}'")

        # Send the prompt to the Hugging Face space and get the response
        response = await query_huggingface_space(prompt)

        # Send the response back to the Discord channel
        await message.channel.send(response)
        print(f"Response sent to Discord: {response}")

# Run the bot
client.run(TOKEN)
