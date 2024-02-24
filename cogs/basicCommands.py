import discord
from discord.ext import commands
import random
import requests


CTX = commands.Context

class BasicCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.hybrid_command(name="hi", description="Responds with 'Hello'.")
    async def hi(self, ctx: CTX):
        await ctx.send("Hello.")



    @commands.hybrid_command(name="animal")
    async def animal(self, ctx):
     animal_types = ['cat', 'dog', 'bird', 'elephant', 'tiger', 'coala', 'panda', 'wolf', 'lion', 'horse', 'Dolphin', 'Bear', 'Fox', 'Deer','Pig', 'Owl' 'Peacock', 'Jellyfish', 'ant', 'bee', 'Butterfly', 'Flamingo','Hippopotamus','Rhinoceros'  ]  # Add more animal types if desired
     random_animal = random.choice(animal_types)

     response = requests.get(f'https://source.unsplash.com/featured/?{random_animal}')
     image_url = response.url

     embed = discord.Embed(title=f"Random {random_animal.capitalize()}", color=discord.Color.blue())
     embed.set_image(url=image_url)

     await ctx.send(embed=embed)

    @commands.hybrid_command(name="slap", description="Slaps a user.")
    async def slap(self, ctx, member: discord.Member):
     # List of GIF URLs
     gif_urls = [
        "https://media.giphy.com/media/Zau0yrl17uzdK/giphy.gif","https://media.tenor.com/Ves8ovceTnUAAAAC/despierta-ya.gif","https://media.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif", "https://media.tenor.com/EzwsHlQgUo0AAAAC/slap-in-the-face-angry.gif","https://media.tenor.com/tKF3HiguDmEAAAAC/wrrruutchxxxxiii-slapt.gif","https://media.tenor.com/2L_eT6hPUhcAAAAC/spongebob-squarepants-patrick-star.gif", "https://media.tenor.com/Sv8LQZAoQmgAAAAC/chainsaw-man-csm.gif", "https://media.tenor.com/k4_iBaFWIAYAAAAC/slapping.gif", "https://tenor.com/view/slap-gif-25249881", "https://tenor.com/view/penguin-penguins-penguin-love-penguin-hug-slapping-gif-24271495", "https://media.tenor.com/5jBuDXkDsjYAAAAC/slap.gif", "https://media.tenor.com/v3M32P68JccAAAAM/shinku-jun.gif", "https://media.tenor.com/Qic0qhw4GoQAAAAM/ultraman-anime.gif", "https://media.tenor.com/mVvQ3NASmsIAAAAM/joe-flacco.gif", "https://media.tenor.com/uTT2gXruNtkAAAAM/oreimo-anime.gif", ""]

      # Selecting a random GIF URL
     random_gif = random.choice(gif_urls)

     # Creating the embed
     embed = discord.Embed(title="Slap!", description=f"{ctx.author.mention} slapped {member.mention}!", color=discord.Color.red())
     embed.set_image(url=random_gif)

     # Sending the embed
     await ctx.send(embed=embed)

    @commands.hybrid_command(name="dad_joke", description="Gives you 1 dad joke")
    async def dadjoke(self, ctx):
      response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
      data = response.json()
      joke = data['joke']
      await ctx.send(joke)


    @commands.hybrid_command(name="avatar", description="Gets a users avatar")
    async def avatar(self, ctx, member: discord.Member = None):
     if not member:
        member = ctx.author

     avatar_url = member.avatar.url
     if avatar_url:
        embed = discord.Embed(
            title="Avatar",
            description=f"The avatar of {member.mention}",
            color=discord.Color.blue()
        )
        embed.set_image(url=avatar_url)
        await ctx.send(embed=embed)
     else:
        await ctx.send(f"{member.mention} does not have an avatar.")



    @commands.hybrid_command(name="ping", description="Returns client latency.")
    async def ping(self, ctx: CTX):
        await ctx.send(f"Pong! Bot latency is ``{round(self.bot.latency * 1000) } ms.``")




async def setup(bot: commands.Bot):
    await bot.add_cog(BasicCommands(bot=bot))