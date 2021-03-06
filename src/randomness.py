import random
import discord
from discord.ext import commands


class Randomness(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Random Number Generator Command
    @commands.command(name="randomnumber")
    async def rand_num(self, ctx, lower_bound=0, upper_bound=0, count=0):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        random_numbers_str = ''
        if count == 0:
            count = 1
        while count > 0:
            number = random.randint(lower_bound, upper_bound)
            random_numbers_str = random_numbers_str + str(number) + ', '
            count -= 1
        random_numbers_str = random_numbers_str[:-2]
        await ctx.message.reply("Your random number(s): " + random_numbers_str)

    # Coin Flip Command
    @commands.command(name="coinflip")
    async def coin_flip(self, ctx):
        if ctx.message.author.bot:  # don't want to take commands from any bots
            return

        flip = random.randint(1, 2)
        if flip == 1:
            await ctx.message.reply('https://cdn.discordapp.com/attachments/883740406469234718/927397534568165436/FlippedHeads.png')
        else:
            await ctx.message.reply('https://cdn.discordapp.com/attachments/883740406469234718/927397541237129216/FlippedTails.png')
