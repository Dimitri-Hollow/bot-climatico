from IPython import embed
import discord
from discord.ext import commands
import requests
import asyncio

# ideia principal: ser uma calculadora para a geração de caborno de uma pessoa

intents = discord.Intents.default()
intents.message_content = True  # Para ler mensagens
bot = commands.Bot(command_prefix="mc!", intents=intents)


@bot.command()
async def carbono_energia(ctx, consumo: float):
    # Calcular a pegada de carbono a partir do consumo de energia elétrica em kWh
    # Fórmula aproximada: 0.0385 kg CO2 por kWh
    pegada_carbono = consumo * 0.0385
    embed = discord.Embed(title="Pegada de Carbono da Energia", description=f"A sua pegada de carbono, por energia, é de {pegada_carbono:.2f} kg CO2.", color=discord.Color.purple())
    embed.set_thumbnail(url="https://img.pikbest.com/origin/09/29/80/87kpIkbEsT4CG.png!w700wp")
    await ctx.send(embed=embed)


@bot.command()
async def carbono_carro(ctx, kilometragem: float):
    # Calcular a pegada de carbono a partir do consumo de energia elétrica em kWh
    # Fórmula aproximada: 0.85 L por km, 1L de gasolina emite aproximadamente 2.31 kg CO2
    pegada_carbono = kilometragem * 0.85 * 2.31
    embed = discord.Embed(title="Pegada de Carbono do Carro", description=f"A sua pegada de carbono, por kilometragem, é de {pegada_carbono:.2f} kg CO2.", color=discord.Color.yellow())
    embed.set_thumbnail(url="https://images.vexels.com/media/users/3/145585/isolated/preview/0cc4204c88694175095d6bda24efb714-vista-lateral-de-carro-de-cidade.png")
    await ctx.send(embed=embed)


bot.run("token")
