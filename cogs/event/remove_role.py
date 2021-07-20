import logging
import discord
from discord import utils
from discord.ext import commands
from discord.ext.commands.context import Context
import config


class RemoveRole(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        super().__init__()
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):

        channel: discord.TextChannel = self.bot.get_channel(int(config.channel))
        message = await channel.fetch_message(int(config.message))
        member: discord.Member = utils.get(message.guild.members, id = payload.user_id)

        
        channel: discord.TextChannel = self.bot.get_channel(int(config.channel))
        message = await channel.fetch_message(int(config.message))
        member: discord.Member = utils.get(message.guild.members, id = payload.user_id)

        try:
            emoji = str(payload.emoji)
            role_remove: discord.Role = utils.get(message.guild.roles, id = config.ROLES_REMOVE[emoji])

            await member.remove_roles(role_remove)
        except Exception as e:
            logging.exception(repr(e))
        finally:
            logging.info(f'{member}' + ' remove role ' + f'{role_remove.name}')

def setup(bot: commands.Bot):
    bot.add_cog(RemoveRole(bot))