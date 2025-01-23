import discord
import random
import os
from discord.ext import commands
import requests
from model import get_class
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola!, soy el bot {bot.user}!')
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)
@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left + right)
@bot.command()
async def minus(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left - right)
@bot.command()
async def multiplied(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left * right)
@bot.command()
async def divided(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left / right)
@bot.command()
async def powered(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send("resultado:",left ** right)
@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir("images"))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)
@bot.command('check')
async def check(ctx):
    if ctx.message.attachments:
        for image in ctx.message.attachments:
            file_name = image.attachments
            file_url = image.url
            await ctx.send(f"imagen guardada en{file_name}")
            await image.save(file_name)
            try:
                class_name = get_class("keras_model.h5","labels.txt", file_name)
                if class_name[0] == "Pigeons":
                    print("Es una paloma")
                    print("Las palomas son aves que se adaptan bien a entornos urbanos y rurales. Son sociales, monógamas y cuidan de sus polluelos juntos. Se alimentan de semillas y restos de comida, y algunas especies, como la paloma mensajera, son conocidas por su habilidad para regresar a su hogar. En muchas culturas simbolizan la paz. Su esperanza de vida es de 3 a 5 años en la naturaleza y más en cautiverio.")
                elif class_name[0] == "Sparrows":
                    print("Es un gorrion")
                    print("Los gorriones son aves pequeñas y sociales que se encuentran en todo el mundo, especialmente en áreas urbanas. Son conocidos por su canto característico y suelen formar grupos. Son monógamos y construyen nidos en árboles o estructuras humanas. Su esperanza de vida es de unos 3 años.")
                elif class_name[0] == "Falcons":
                    print("Es un halcon")
                    print("Los halcones son aves rapaces rápidas y con excelente visión, que cazan principalmente aves y pequeños mamíferos. Son solitarios y territoriales, y anidan en acantilados, árboles o estructuras humanas. Su esperanza de vida es de 15 a 20 años en la naturaleza.")
                elif class_name[0] == "Gulls":
                    print("Es una gaviota")
                    print("Las gaviotas son aves costeras sociales y oportunistas, que se alimentan de peces, restos de comida y pequeños animales. Se encuentran cerca del mar y en zonas urbanas, y su esperanza de vida es de 10 a 15 años.")
                elif class_name[0] == "Toucans":
                    print("Es un tucan")
                    print("Los tucanes son aves tropicales con un pico colorido, que viven en bosques de América Central y Sudamérica. Son frugívoros y sociales, anidan en huecos de árboles. Su esperanza de vida es de 10 a 20 años.")
                elif class_name[0] == "Parrots":
                    print("Es un loro")
                    print("Los loros son aves inteligentes y sociales, con picos curvos y colores brillantes. Viven en regiones tropicales y se alimentan de frutas y semillas. Pueden imitar sonidos y tienen una esperanza de vida de 20 a 50 años.")
            except:
                await(ctx.send("No se leyo bien la imagen"))
    else:
        await(ctx.send("no subiste imagen 0_0"))


bot.run("Tu Token")
