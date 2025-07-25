import discord
import asyncio
from discord import app_commands

TOKEN = "12345678910"         # BOT TOKEN
GUILD_ID = 12345678910        # 伺服器ID

intents = discord.Intents.default()
meow_bot = discord.Client(intents=intents)
tree = app_commands.CommandTree(meow_bot)

# 函式 countdown()
async def countdown(interaction: discord.Interaction, 標題: str, 分鐘數: int, 提醒對象們: str):
    await interaction.response.defer(thinking=True)
    await interaction.followup.send(
        f"⏳ 開始倒數 {分鐘數} 分鐘：**{標題}**\n🔔 到時我會提醒：{提醒對象們.strip()}"
    )
    await asyncio.sleep(分鐘數 * 60)
    await interaction.channel.send(
        f"⏰ {分鐘數} 分鐘到了！\n📣 **{標題}**（{提醒對象們.strip()}）"
    )

@meow_bot.event
async def on_ready():
    cmd = app_commands.Command(
        name="計時器",
        description="倒數 X 分鐘後提醒（支援多個 @使用者 或 @身分組）",
        callback=countdown
    )
    tree.add_command(cmd, guild=discord.Object(id=GUILD_ID))
    await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f"✅ Bot 上線：{meow_bot.user}，Slash 指令已同步")

# 啟動 Bot
meow_bot.run(TOKEN)
