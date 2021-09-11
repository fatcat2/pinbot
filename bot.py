import os

import discord


intents = discord.Intents(messages=True, guilds=True, reactions=True)

class MyClient(discord.Client):
    pinz = None
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

        self.pinz = client.get_channel(int(os.getenv("PIN_CHANNEL")))

        if self.pinz is not None:
            print("Found pinz channel")

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        pin_reacts = list(filter(lambda react: str(react) == "📌", reaction.message.reactions))
        if str(reaction.emoji) == "📌" && len(pin_reacts) == 0:
            await self.pinz.send(
                    "> " + 
                    reaction.message.content + 
                    "\nBy " + 
                    reaction.message.author.mention + ", " + 
                    reaction.message.created_at.strftime("%m/%d/%Y, %H:%M:%S"))


client = MyClient()
client.run(os.getenv("DISCORD_KEY"))

