import discord
from discord.ext import commands
import time
import datetime
import wavelink


class Music(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.hybrid_command(name="play", description="Play a song in your voice channel.")
    async def play(self, ctx, search: str):
     if (ctx.author.voice):
        query = await wavelink.YouTubeTrack.search(search)
        destination = ctx.author.voice.channel

        if not ctx.guild.voice_client:
            vc = await destination.connect(cls=wavelink.Player)
        else:
            vc = ctx.guild.voice_client

        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(query[0])  # Select the first track from the query list
            await ctx.send(f"Now playing {vc.current.title}.")
        else:
            await vc.queue.put_wait(query[0])  # Select the first track from the query list
            await ctx.send("Song was added to queue.")
     else:
        await ctx.send("You are not in voice channel.")


    @commands.hybrid_command(name="all_i_want_for_christmas", description="Plays All I want for Chirstmas is you")
    async def playinh(self, ctx):
     if (ctx.author.voice):
        query = await wavelink.YouTubeTrack.search("https://www.youtube.com/watch?v=RmUWWVZw28E")
        destination = ctx.author.voice.channel

        if not ctx.guild.voice_client:
            vc = await destination.connect(cls=wavelink.Player)
        else:
            vc = ctx.guild.voice_client

        if vc.queue.is_empty and not vc.is_playing():
            await vc.play(query[0])  # Select the first track from the query list
            await ctx.send(f"Now playing {vc.current.title}.")
        else:
            await vc.queue.put_wait(query[0])  # Select the first track from the query list
            await ctx.send("Song was added to queue.")
     else:
        await ctx.send("You are not in voice channel.")

    @commands.hybrid_command(name="skip", description="Skips to the next song.")
    async def skip(self, ctx):

        vc = ctx.guild.voice_client
        await vc.stop()
        await ctx.send("Song was skipped.")

    @commands.hybrid_command(name="pause", description="Pauses the player.")
    async def pause(self, ctx):

        vc = ctx.guild.voice_client

        if vc.is_playing():

            await vc.pause()
            await ctx.send("Song is paused.")
        else:
            await ctx.send("The song is already paused.")

    @commands.hybrid_command(name="resume", description="Unpauses the player.")
    async def resume(self, ctx):

        vc = ctx.guild.voice_client

        if vc.is_playing():
         await ctx.send("Song is already playing.")
        else:
         await  vc.resume()
         await ctx.send("The song is resumed.")

    @commands.hybrid_command(name="disconnect", description="Stops the player and leaves the voice chat.")
    async def disconnect(self, ctx):
        vc = ctx.guild.voice_client
        await vc.disconnect()
        await ctx.send("Bot is disconnected.")


    @commands.hybrid_command(name="queue", description="Displays a current queue of tracks.")
    async def queue(self, ctx):
        vc = ctx.guild.voice_client
        if not vc.queue.is_empty:
            song_counter = 0
            songs = []
            Queue = vc.queue.copy()
            embed = discord.Embed(title="Queue", color=discord.Colour.random())
            for song in Queue:  # Changed 'queue' to 'Queue'
                song_counter += 1
                songs.append(song)
                embed.add_field(name=f"[{song_counter}] Duration {song.duration}", value=f"{song.title}", inline=False)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Queue is empty.")


async def setup(bot: commands.Bot):
    await bot.add_cog(Music(bot=bot))