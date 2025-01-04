import discord
from discord.ext import commands, tasks

TOKEN = "Your token"

intents = discord.Intents.default()
intents.voice_states = True  
intents.members = True      

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot đã đăng nhập với tên: {bot.user}")
    print("Đã sẵn sàng giám sát voice channel.")
    auto_mute.start()

@tasks.loop(seconds=30)
async def auto_mute():
    for guild in bot.guilds:
        for vc in guild.voice_channels:
            if vc.members:
                print(f"Đang xử lý voice channel: {vc.name}")

                for member in vc.members:
                    if not member.bot: 
                        try:
                            await member.edit(mute=True, reason=f"Tự động mute")
                            print(f"Đã mute: {member.display_name} trong voice channel {vc.name}")

                        except discord.Forbidden:
                            print(f"Không có quyền mute {member.display_name}.")

                        except Exception as e:
                            print(f"Lỗi khi mute {member.display_name}: {e}")

bot.run(TOKEN)
