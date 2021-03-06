import discord
from discord.ext import commands
from whois import whois

class Whois(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command(name='whois')
    async def whodomain(self, ctx, domain):
        target = whois(domain)
        embed = discord.Embed(
            title = 'Informações de domínio',
            colour= 0xb72ce6
        )
        embed.add_field(name='Nome do domínio', value=target['domain_name'])
        embed.add_field(name='Data de criação', value=target['creation_date'], inline=False)
        embed.add_field(name='País de registro', value=target['country'], inline=False)
        embed.add_field(name='Cidade de registro', value=target['city'])
        embed.set_footer(text='Nota: DATA REDACTED significa que o domínio não disponiliza publicamente essas informações')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Whois(bot))