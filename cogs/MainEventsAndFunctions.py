from typing import Any
import discord
from discord.ext import commands
from colorama import Fore,Back,Style
from discord.interactions import Interaction
from discord.ui import Select, View, Button
import time
import platform
import wavelink

class MainFunctionAndEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(connect_to_node(self=self))
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="The Dom Empire")) 
        print(" NO NO")
        prfx3 = (Fore.YELLOW + "\n -------------------------------------------")
        prfx2 = (Back.RESET + Fore.LIGHTMAGENTA_EX )
        prfx = (Back.LIGHTBLUE_EX + Fore.RED + time.strftime("%H:%M:%S GMT", time.gmtime()) + Back.RESET + Fore.WHITE + Style.NORMAL + Style.BRIGHT)
        print(prfx + " Logged in as: " + prfx2 + self.bot.user.name + prfx3)
        print(prfx + " Bot ID: " + prfx2 + str(self.bot.user.id) + prfx3)
        print(prfx + " Discord version: " + prfx2 + discord.__version__ + prfx3)
        print(prfx + " Python version: " + prfx2 + str(platform.python_version()) + prfx3)
        try:
         synced = await self.bot.tree.sync()
         print(prfx + " Slash Commands Synced " + prfx2 + str(len(synced)) + " Commands " + prfx3)
        except Exception as e:
         print(prfx + " Error with:  " + prfx2 + e + " Commands" + prfx3 + "-------------------------------------" )
        print(Fore.RESET + Back.RESET + Style.RESET_ALL)

        #prfx = (Back.BLACK + Fore.GREEN + time.strftime("%H:%M:%S UTC", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)
        #print(prfx + "Logged in as " + Fore.YELLOW + self.bot.user.name)
        #print(prfx + "Bot ID " + Fore.YELLOW + str(self.bot.user.id))
        #print(prfx + "Discord version" + Fore.YELLOW + discord.__version__)
        #print(prfx + "Python version" + Fore.YELLOW + str(platform.python_version())) 
        #print("--------------------------")
        #try:
        # synced = await self.bot.tree.sync()
        # print(f"Synced {len(synced)} commands.")
        #except Exception as e:
        # print(f"Error with commands: {e}")

    #@commands.hybrid_command(name="try")
    #async def test(ctx):
    #   ctx.send("hi")


    #MEMBER JOIN EVENT

    #@commands.Cog.listener()
    #async def on_member_join(self, member:discord.Member):
    # channel = self.bot.get_channel(1149612662121058364)
    # await channel.send(f"Hi **{member}**, welcome to our server!")

    #MEMBER LEAVE EVENT

   # @commands.Cog.listener()
   # async def on_member_remove(self, member):
   #   await member.send("test")
   #   channel = self.bot.get_channel(1149612662121058364)
   #   await channel.send(f"Goodbye {member}.")


async def connect_to_node(self):
    node = wavelink.Node(uri="test-lavalink.herokuapp.com", password="youshallnotpass", secure=False)
    await wavelink.NodePool.connect(client=self.bot, nodes=[node])
    wavelink.Player.autoplay = True




class HelpCommand(Select):
    def __init__(self, bot: commands.Bot):
       super().__init__(
          placeholder="Chose a category",
          options=[
             discord.SelectOption(label=cog_name,description=cog.__doc__)
             for cog_name, cog in bot.cogs.items() if cog.__cog__commands__ and cog_name not in ['jishaku']])
       self.bot = bot

    async def callback(self, interaction: discord.Interaction) -> None:
       cog = self.bot.get_cog(self.values[0])
       assert cog

       commands_mixer = []
       for i in cog.walk_commands():
          commands_mixer.append(i)

       for i in cog.walk_app_commands():
          commands_mixer.append(i)

       embed = discord.Embed(title=f"{cog.__cog_name__} Commands", description='\n'.join(f"**{command.name}**: `{command.description}`" for command in commands_mixer))
       await interaction.response.send_message(embed=embed, ephemeral=True)



    @commands.hybrid_command(name="help", description="helps you with bot")
    async def help(self, ctx: commands.Context):
       embed = discord.Embed(title="Help command ", description="none")
       view = View.add_item(HelpCommand(self.bot))
       await ctx.send(embed=embed, ephemeral=True)



async def setup(bot: commands.Bot):
    await bot.add_cog(MainFunctionAndEvents(bot=bot))
