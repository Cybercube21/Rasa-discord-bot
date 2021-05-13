import discord
import requests
import os

from rasa_connection import curl_request
from dotenv import load_dotenv

#Load Discord Bot Token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
client = discord.Client()

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')

#Wait for a new Message
@client.event
async def on_message(message):
	#Verify that the User is not the Bot itself
	if message.author != client.user:

		#Use curl_request Function (located in rasa_connection.py)
		answers = curl_request(message.content, str(message.author))

		#Insert all Respons into one String so we can return it into the Discord Channel
		end_response = " \n ".join((answers))

		#Return the message in a Discord Channel
		return await message.channel.send(f'{message.author.mention} ' + end_response)

client.run(token)