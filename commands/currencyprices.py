import discord
import requests
from discord.ext import commands
from time import strftime
class Cott(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='dola', aliases=['dolar', 'brlusd'])
    async def valor_dola(self, ctx, quantia=1.00): #quantia=1.00, ou seja, se o valor não for especificado a cotação será multiplicada por 1
        cotação = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL").json()
        valor = float(cotação['USDBRL']['bid'])
        
        embed = discord.Embed(
            title='Cotação do Dólar Americano frente ao Real Brasileiro',
            color=0x03f0fc 
            )
        embed.add_field(name='Valor em Dólares Americanos (USD)', value=f'U${quantia:.2f}', inline=False)
        embed.add_field(name='Valor em Reais Brasileiros (BRL)', value=f"R${valor*quantia:.2f}", inline=False)
        embed.set_footer(text=f'Dados de {strftime("%d/%m/%Y || %H:%M")}')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Cott(bot))