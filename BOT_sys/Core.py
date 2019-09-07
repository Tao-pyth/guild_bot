# インストールした discord.py を読み込む
import discord

# 自分のBotのアクセストークンに置き換えてください
TOKEN = '********************************'

# 接続に必要なオブジェクトを生成
client = discord.Client()

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    CHANNEL_ID = ?-----------------?
    channel = client.get_channel(CHANNEL_ID)
    await channel.send("こんにちわ。本日の業務を開始します")

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    if message.content == '/cleanup':
        if message.author.guild_permissions.administrator:
            await message.channel.purge()
            await message.channel.send('塵一つ残らないね！')
        else:
            await message.channel.send('何様のつもり？')
    await message.channel.send(message.content)
    await client.logout()
    exit()

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)
