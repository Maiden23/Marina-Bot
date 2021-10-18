
import discord 
import os



client = discord.Client()


characters = ["Glitch","Zawardo","timeleaper","morph"]
glitch = "Arigato. I have psychi powers and i hope i can help you:)"
zawardo = "Gracias .I Have the power to manipulate all 5 elements. Let's give it all. "
timeleaper = "Merci .I can mainpulate time. Let's change time together . " 
morph = "Grazie . I have the power to change from one form to another. "
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


  if message.content.startswith("$characters" ):
     await message.channel.send(characters)
   
  if message.content.startswith("$glitch"):
    await message.channel.send(glitch)
    
  if message.content.startswith("$zawardo"):
    await message.channel.send(zawardo)

  if message.content.startswith("$timeleaper"):
    await message.channel.send(timeleaper)

  if message.content.startswith("$morph" ):
    await message.channel.send(morph)

client.run(os.getenv("work"))



     









