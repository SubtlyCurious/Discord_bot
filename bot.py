import discord

class MyClient(discord.Client):
    
    async def on_ready(self):
      print(f'logged in as {self.user} {ID: {self.user.id}')

    async def on_message(self, message):
      
      if message.author.id == self.user.id:
          return
      
      if message.content.startswith('!hello'):
          await message.channel.send('Hello {}'.format(message.author.name))

client = MyClient()
client.run('token')
