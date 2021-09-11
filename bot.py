import os

import discord


intents = discord.Intents(messages=True, guilds=True, reactions=True)

def create_embed(message):
        embed_dict = {
                "embed": {
                    "title": "it's a pin!",
                    "description": f"{message.author.mention} said this at [{message.created_at.strftime('%m/%d/%Y, %H:%M:%S')}]({message.jump_url})\n```{message.content}```",
                    "color": 12656255,
                    "footer": {
                        "icon_url": "https://cdn.discordapp.com/embed/avatars/0.png",
                        "text": "pinned by @guoboro"
                        }
                    }
                }
        embed = discord.Embed.from_dict(embed_dict)
        print(embed)
        return embed

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
        print(pin_reacts)
        if str(reaction.emoji) == "📌" and len(pin_reacts) == 1:
            embed_description = f"{reaction.message.author.mention} said this at [{reaction.message.created_at.strftime('%m/%d/%Y, %H:%M:%S')}]({reaction.message.jump_url})\n```{reaction.message.content}```"
            my_embed = discord.Embed(title="It's a pin!", description=embed_description, colour=discord.Colour.from_rgb(171, 35, 48))
            my_embed.set_footer(icon_url="https://cdn.discordapp.com/embed/avatars/0.png", text = "pinned by @guoboro")

            await self.pinz.send(embed=my_embed)


client = MyClient()
client.run(os.getenv("DISCORD_KEY"))

