import discord
import random
import json
from discord.ext import commands
from utils.tools import *
from utils.config import Config
from utils import checks
from utils.language import Language
config = Config()

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
bot = commands.Bot(description="Bot prefix is *", command_prefix=commands.when_mentioned_or("*" ), pm_help = True)
client.remove_command('help')


# This is the limit to how many posts are selected
limit = config.max_nsfw_count

@client.event
async def on_ready():
     print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
     print('the bot is ready')
     print('.......')
     print('created by gaurav and bluebird')

class NSFW():
    def __init__(self, bot):
        self.bot = bot

    @checks.is_nsfw_channel()
    @commands.command()
    async def rule34(self, ctx, *, tags:str):
        await ctx.channel.trigger_typing()
        try:
            data = requests.get("http://rule34.xxx/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit, tags), headers=header).json()
        except json.JSONDecodeError:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return

        count = len(data)
        if count == 0:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        image_count = 4
        if count < 4:
            image_count = count
        images = []
        for i in range(image_count):
            image = data[random.randint(0, count)]
            images.append("http://img.rule34.xxx/images/{}/{}".format(image["directory"], image["image"]))
        await ctx.send(Language.get("nsfw.results", ctx).format(image_count, count, tags, "\n".join(images)))

    @checks.is_nsfw_channel()
    @commands.command()
    async def e621(self, ctx, *, tags:str):
        """Searches e621.net for the specified tagged images"""
        await ctx.channel.trigger_typing()
        try:
            data = requests.get("https://e621.net/post/index.json?limit={}&tags={}".format(limit, tags), headers=header).json()
        except json.JSONDecodeError:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        count = len(data)
        if count == 0:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        image_count = 4
        if count < 4:
            image_count = count
        images = []
        for i in range(image_count):
            images.append(data[random.randint(0, count)]["file_url"])
        await ctx.send(Language.get("nsfw.results", ctx).format(image_count, count, tags, "\n".join(images)))

    @checks.is_nsfw_channel()
    @commands.command()
    async def yandere(self, ctx, *, tags:str):
        """Searches yande.re for the specified tagged images"""
        await ctx.channel.trigger_typing()
        try:
            data = requests.get("https://yande.re/post/index.json?limit={}&tags={}".format(limit, tags), headers=header).json()
        except json.JSONDecodeError:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        count = len(data)
        if count == 0:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        image_count = 4
        if count < 4:
            image_count = count
        images = []
        for i in range(image_count):
            images.append(data[random.randint(0, count)]["file_url"])
        await ctx.send(Language.get("nsfw.results", ctx).format(image_count, count, tags, "\n".join(images)))

    @checks.is_nsfw_channel()
    @commands.command()
    async def danbooru(self, ctx, *, tags:str):
        """Searches danbooru.donmai.us for the specified tagged images"""
        await ctx.channel.trigger_typing()
        try:
            data = requests.get("https://danbooru.donmai.us/post/index.json?limit={}&tags={}".format(limit, tags), headers=header).json()
        except json.JSONDecodeError:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        count = len(data)
        if count == 0:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        image_count = 4
        if count < 4:
            image_count = count
        images = []
        for i in range(image_count):
            try:
                images.append(data[random.randint(0, count)]["file_url"])
            except KeyError:
                await ctx.send(data["message"])
                return
        await ctx.send(Language.get("nsfw.results", ctx).format(image_count, count, tags, "\n".join(images)))

    @checks.is_nsfw_channel()
    @commands.command()
    async def gelbooru(self, ctx, *, tags:str):
        """Searches gelbooru.com for the specified tagged images"""
        await ctx.channel.trigger_typing()
        try:
            data = requests.get("https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit, tags), headers=header).json()
        except json.JSONDecodeError:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        count = len(data)
        if count == 0:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        image_count = 4
        if count < 4:
            image_count = count
        images = []
        for i in range(image_count):
            try:
                images.append("{}".format(data[random.randint(0, count)]["file_url"]))
            except KeyError:
                await ctx.send(data["message"])
                return
        await ctx.send(Language.get("nsfw.results", ctx).format(image_count, count, tags, "\n".join(images)))

    @checks.is_nsfw_channel()
    @commands.command()
    async def xbooru(self, ctx, *, tags: str):
        """Searches xbooru.com for the specified tagged images"""
        await ctx.channel.trigger_typing()
        try:
            data = requests.get("https://xbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit={}&tags={}".format(limit, tags),  headers=header).json()
        except json.JSONDecodeError:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        count = len(data)
        if count == 0:
            await ctx.send(Language.get("nsfw.no_results_found", ctx).format(tags))
            return
        image_count = 4
        if count < 4:
            image_count = count
        images = []
        for i in range(image_count):
            try:
                post = data[random.randint(0, count)]
                images.append("http://img3.xbooru.com/images/{}/{}".format(post["directory"], post["image"]))
            except KeyError:
                await ctx.send(data["message"])
                return
        await ctx.send(Language.get("nsfw.results", ctx).format(image_count, count, tags, "\n".join(images)))

def setup(bot):
     bot.add_cog(NSFW(bot))






bot.run(os.getenv('Token'))
