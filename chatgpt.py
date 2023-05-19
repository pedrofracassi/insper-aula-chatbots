import openai
import chaves

openai.api_key = chaves.CHATGPT_KEY

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "O que é o Insper?"},
    ]
)

print(response.choices[0].message.content)