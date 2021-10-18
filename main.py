
import discord 
import os
import json
import colour


client = discord.Client()
embed=discord.Embed(title="Characters",description="1.Glitch - I have the power to control mind ,  2.Zawardo- I can manipulate 5 elements of the world ,3. timeleaper- I can manipulate time in a blink of an eye ,4. morph- I can shift from one form to another ",colour=discord.Colour.gold())

embed1 = discord.Embed(title="Glitch", description="Arigato, Let's have fun killing", colour= discord.Colour.blue())
embed2 = discord.Embed(title="Zawardo", description="Gracias, Let's give it all. ", colour=discord.Colour.red())
embed3= discord.Embed(title="timeleaper" ,description= "Merci, Let's change time together . ", colour=discord.Colour.green())
embed4= discord.Embed(title="morph" ,description= "Grazie , Looking forward to working with you ",colour=discord.Colour.purple())
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
  if message.content.startswith("$sup"):
    await message.channel.send("Nothing much , how about you?!")


  if message.content.startswith("$characters"):
      
        await message.channel.send(embed=embed)
   
  if message.content.startswith("$glitch"):
    await message.channel.send(embed=embed1)
    
  if message.content.startswith("$zawardo"):
    await message.channel.send(embed=embed2)

  if message.content.startswith("$timeleaper"):
    await message.channel.send(embed=embed3)

  if message.content.startswith("$morph" ):
    await message.channel.send(embed=embed4)

client.run(os.getenv("work"))



     









