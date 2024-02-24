from flask import Flask, render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return '''<body style="margin: 0; padding: 0;">
    <iframe width="100%" height="100%" src="https://axocoder.vercel.app/" frameborder="0" allowfullscreen></iframe>
  </body>'''

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()

keep_alive()
print("Server Running Because of Axo")

import discord
from discord.ext import commands

from discord.ext.commands import has_permissions

class CustomCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.hybrid_command(name="wwraid", description="Hosts a raid on Wizard Wars")
    @has_permissions(manage_events=True)
    async def WWRaid(self, ctx: commands.Context, member: discord.Member):
        embed = discord.Embed(
        title="RAID ON WIZARD WARS!", url="https://www.roblox.com/games/5951776961/Wizard-Wars-RANKED#ropro-quick-play",
        description=f"Host: {member.mention} \n GET UR AVATAR AND KILL ALL NON DOMS! \n RECRUIT AS MANY PEOPLE AS YOU CAN! \n GAME: https://www.roblox.com/games/5951776961/Wizard-Wars-RANKED#ropro-quick-play",
        color=discord.Color.red())
        embed.set_image(url="https://cdn.discordapp.com/attachments/1105826924896464987/1105832916031901897/dom.png")
        await ctx.guild.get_channel(1105578746339151953).send("@everyone")
        await ctx.guild.get_channel(1105578746339151953).send(embed=embed)

    @WWRaid.error
    async def WWRaid_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Permission Error",
            description="You don't have permission to host. Make sure that you have 'Manage Members' permission on your role.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)


    @commands.hybrid_command(name="training", description="Hosts a training in wizard wars")
    async def Training(self, ctx: commands.Context, member: discord.Member, code: str):
        embed = discord.Embed(
        title="Training time!", url="https://www.roblox.com/games/5951776961/Wizard-Wars-RANKED#ropro-quick-play",
        description=f"Host: {member.mention} \n GET UR AVATAR \n SERVER CODE:{code} \n GAME: \n https://www.roblox.com/games/5951776961/Wizard-Wars-RANKED#ropro-quick-play",
        color=discord.Color.red())
        embed.set_image(url="https://cdn.discordapp.com/attachments/1105826924896464987/1105832916031901897/dom.png")
        await ctx.guild.get_channel(1105724570532585512).send("@everyone")
        await ctx.guild.get_channel(1105724570532585512).send(embed=embed)    

    @Training.error
    async def CRRaid_error(self, ctx, error):
     if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Permission Error",
            description="You don't have permission to host. Make sure that you have 'Manage Members' permission on your role.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(CustomCommands(bot=bot))