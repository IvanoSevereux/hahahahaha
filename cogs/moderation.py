import discord
from discord.ext import commands
import time
import datetime




from discord.ext.commands import has_permissions

class Moderation(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.hybrid_command(name="kick", description="Kick a user from the server")
    @has_permissions(kick_members = True)
    async def kick(self ,ctx: commands.Context, member: discord.Member, *, reason = None):
     if reason == None:
        await member.send(f"You are kicked from '{ctx.guild.name}' with reason: {reason}.")
        reason = f"{member} is being kicked by {ctx.message.author} with no reason provided."
        await member.kick(reason=reason)
        embed = discord.Embed(
        title="User Kicked",
        description=f"User {member.mention} has been successfully kicked.",
        color=discord.Color.green())
        embed.add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)
     else:
        await member.send(f"You are kicked from '{ctx.guild.name}' with reason: {reason}.")
        await member.kick(reason=reason)


        embed = discord.Embed(
        title="User Kicked",
        description=f"User {member.mention} has been successfully kicked.",
        color=discord.Color.green())
        embed.add_field(name="Reason", value=reason)
        await ctx.send(embed=embed)

    @kick.error

    async def kick_error(ctx, error):
     if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            title="Permission Error",
            description="You don't have permission to kick members.",
            color=discord.Color.red()
        )
        await ctx.send(embed=embed)





    @commands.hybrid_command(name="ban", description="Ban a user from the server")
    @has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, member: discord.Member, *, reason=None):
     if not reason == None:
        await member.send(f"You are banned from '{ctx.guild.name}' with reason: {reason}.")
        await member.ban(reason=reason)

        embed = discord.Embed(
            title="User Banned",
            description=f"User {member.mention} has been successfully banned.",
            color=discord.Color.green()
        )
        embed.add_field(name="Reason", value=reason)

        await ctx.send(embed=embed)
     else:
        await member.send(f"You are banned from '{ctx.guild.name}' with reason: {reason}.")
        reason = f"{member} was banned by {ctx.message.author}."
        await member.ban(reason=reason)


        embed = discord.Embed(
            title="User Banned",
            description=f"User {member.mention} has been successfully banned.",
            color=discord.Color.green()
        )
        embed.add_field(name="Reason", value=reason)

        await ctx.send(embed=embed)


    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permission Error",
                description="You don't have permission to ban members.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed) 





    @commands.hybrid_command(name="unban", description="Unban a banned user from the server")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userid):
      user = discord.Object(id=userid)
      await ctx.guild.unban(user)
      embed = discord.Embed(
            title="User Unbanned",
            description=f"User has been successfully unbanned.",
            color=discord.Color.green())
      await ctx.send(embed=embed)

    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permission Error",
                description="You don't have permission to unban members.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed) 


    @commands.hybrid_command(name="role_add", description="Add a role to a user")
    @has_permissions(manage_roles=True)
    async def addrole(self, ctx, user : discord.Member, role: discord.Role):

        if role in user.roles:
            alrEmbed = discord.Embed(
                title="ERROR",
                description=f"{user.mention} already have {role.mention} role.",
                color=discord.Colour.red()
            )
            await ctx.send(embed=alrEmbed)
        else:
            await user.add_roles(role)
            aembed= discord.Embed(
            title= "Success!",
            description=f"**{user.mention}** recieved **{role.mention}** role.",
            color=discord.Color.green())
            await ctx.send(embed=aembed)

    @addrole.error
    async def addroleError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            Erembed = discord.Embed(
                title="Permission Error",
                description="You don't have permission to Manage Roles.",
                color=discord.Color.red())
            ctx.send(embed=Erembed)



    @commands.hybrid_command(name="role_remove", description="remove a role from a user")
    @has_permissions(manage_roles=True)
    async def roleremove(self, ctx, user : discord.Member, role: discord.Role):

        if role in user.roles:

            await user.remove_roles(role)
            aembed= discord.Embed(
            title= "Success!",
            description=f"** Removed {role.mention} role from {user.mention}**",
            color=discord.Color.green())
            await ctx.send(embed=aembed)
        else:
            alrEmbed = discord.Embed(
            title="ERROR",
            description=f"{user.mention} Doesn't have {role.mention} role.",
            color=discord.Colour.red()
            )
            await ctx.send(embed=alrEmbed)

    @roleremove.error
    async def roleremoveError(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            Erembed = discord.Embed(
                title="Permission Error",
                description="You don't have permission to Manage Roles.",
                color=discord.Color.red())
            ctx.send(embed=Erembed)




    @commands.hybrid_command(name="mute", description="Mute a member, with an optional time limit.")
    #@has_permissions(mute_members=True)
    async def mute(self, ctx ,member: discord.Member, timelimit):
        embed= discord.Embed(title="Success!", description=f"{member.mention} got timeouted for {timelimit}.", color= discord.Color.green())
        if "s" in timelimit:
            gettime = timelimit.strip("s")
            newtime = datetime.timedelta(seconds=int(gettime))
            #await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            #await ctx.send(embed=embed)
        elif "m" in timelimit:
            gettime = timelimit.strip("m")
            newtime = datetime.timedelta(minutes=int(gettime))
           # await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
           # await ctx.send(embed=embed)
        elif "h" in timelimit:
            gettime = timelimit.strip("h")
            newtime = datetime.timedelta(hours=int(gettime))
           # await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
           # await ctx.send(embed=embed)
        elif "d" in timelimit:
            gettime = timelimit.strip("d")
            newtime = datetime.timedelta(days=int(gettime))
            #await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            #await ctx.send(embed=embed)
        elif "w" in timelimit:
            gettime = timelimit.strip("w")
            newtime = datetime.timedelta(weeks=int(gettime))
            #await member.edit(timed_out_until=discord.utils.utcnow() + newtime)
            #await ctx.send(embed=embed)
        await ctx.send("Coming soon...")


    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            embed = discord.Embed(
                title="Permission Error",
                description="You don't have permission to Timeout members.",
                color=discord.Color.red()
            )
            await ctx.send(embed=embed)



async def setup(bot: commands.Bot):
    await bot.add_cog(Moderation(bot=bot))