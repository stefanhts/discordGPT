import openai
import os
import discord

from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.getenv("DISCORD_TOKEN")


#response = openai.ChatCompletion.create(
#    model="gpt-3.5-turbo",
#    messages=[
#            {"role": "system", "content": "You are a discord chat bot named boibot"},
#            {"role": "user", "content": "Why should DevOps engineer learn kubernetes?"},
#        ]
#)

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return
        else:
            print(message.content)
            if message.content.startswith('!boi'):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                            {"role": "system", "content": "You are a discord chat bot named boibot"},
                            {"role": "user", "content": message.content},
                        ]
                )
                await message.channel.send(response['choices'][0]['message']['content'])

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(token)

