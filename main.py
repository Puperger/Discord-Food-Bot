import discord
import random
import json



intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

f = open("food.json", "r")
print("loaded")

#f.write("{}")
foodlist = json.load(f)

f.close()


@client.event
async def on_ready():
    print(f"looged in as {client.user}")


@client.event
async def on_message(message):
    if message.content.startswith(".food"):
        dish = random.choice(foodlist)
        food = dish["name"]
        
        out = food + "\nIngredients:"

        for i in dish["ingredients"]:
            out += f"\n • {i}"
        

        await message.channel.send(out)



client.run("NzYzNzUyNzY4NjY1MDI2NTcw.GU-kps.Yje7OaXucsX6biEaCU9Vk20_dYzQEHP3NprC8A")
