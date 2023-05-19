import discord

from chaves import DISCORD_TOKEN

import json
from ibm_watson import AssistantV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import chaves

watson_api_key = chaves.WATSON_API_KEY
workspace_id = chaves.WATSON_WORKSPACE_ID

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

authenticator = IAMAuthenticator(watson_api_key)
assistant = AssistantV1(version='2021-11-27', authenticator=authenticator)
assistant.set_service_url('https://api.us-south.assistant.watson.cloud.ibm.com/instances/9f353bed-9a4a-4aa6-980c-2f4d392785dc')
assistant.set_http_config({'timeout': 100})

@client.event
async def on_ready():
    print('TÁ PRONTO O SORVETINHO')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = assistant.message(workspace_id=workspace_id, input={'text': message.content}).get_result()
    await message.channel.send(response['intents'][0]['intent'])

client.run(DISCORD_TOKEN)
