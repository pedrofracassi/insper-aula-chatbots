import discord

from chaves import DISCORD_TOKEN

import json

import chaves

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

import openai
openai.api_key = chaves.CHATGPT_KEY

@client.event
async def on_ready():
    print('TÁ PRONTO O SORVETINHO')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    response = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "Seu nome é João e você estuda no Insper."},
            {"role": "user", "content": message.content},
        ]
    )

    await message.channel.send(response.choices[0].message.content)

client.run(DISCORD_TOKEN)
