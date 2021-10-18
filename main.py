
import discord 
import os



client = discord.Client()


characters = ["Glitch","Zawardo","timeleaper","morph"]
glitch = "Thank you for choosing me , I have psychi powers and i hope i can help you:)"

@client.event
async def on_ready():
  print('Hello {0.user}'.format (client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("$hello"):
    await message.channel.send("Hello")  
    return


  if message.content.startswith("$characters"):
  
    await message.channel.send(characters)
   
  if message.content.startswith("$Glitch"):
    await message.channel.send(glitch)
    
  

client.run(os.getenv("work"))



     









