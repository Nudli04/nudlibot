import discord
import requests
import json

client = discord.Client()

@client.event
async def on_ready():
  print('Bejelentkeztem {0.user} -ként'.format(client))

def get_price():
  response = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=DOGEUSDT")
  json_data= response.json()
  price = json_data['lastPrice']
  return(price)

def get_prchange():
  response = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=DOGEUSDT")
  json_data= response.json()
  prchange = json_data['priceChangePercent']
  return(prchange)

def get_phigh():
  response = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=DOGEUSDT")
  json_data= response.json()
  phigh = json_data['highPrice']
  return(phigh)

def get_plow():
  response = requests.get("https://api.binance.com/api/v3/ticker/24hr?symbol=DOGEUSDT")
  json_data= response.json()
  plow = json_data['lowPrice']
  return(plow)


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.author.id == 159985870458322944 and message.content.startswith('GG'):
    mention = message.mentions[0].id
    response = f"Én is gratulálok neked <@!{mention}>, ügyes vagy"
    await message.channel.send(response)
  
  if message.content.startswith('$doge'):
        price = get_price()
        prchange = get_prchange()
        phigh = get_phigh()
        plow = get_plow()
        await message.channel.send(f"----------DOGECOIN----------\nJelenlegi ár: {price:.7}  USD\nNapi változás: {prchange} %\nMai legmagasabb ár: {phigh:.7} USD\nMai legalacsonyabb ár: {plow:.7} USD\n-----------------------------------")
  
client.run(TOKEN)

