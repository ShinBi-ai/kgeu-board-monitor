from discord_webhook import DiscordWebhook, DiscordEmbed

from config import DISCORD_WEBHOOK_URL


def send_notification(post):
    webhook = DiscordWebhook(url=DISCORD_WEBHOOK_URL)

    embed = DiscordEmbed(
        title=post["title"],
        url=post["url"],
        description="📢 **노조 게시판에 새 게시글이 등록되었습니다.**",
        color="2F80ED",
    )

    embed.add_embed_field(
        name="👤 작성자",
        value=post["writer"],
        inline=True,
    )

    embed.add_embed_field(
        name="📅 작성일",
        value=post["date"],
        inline=True,
    )

    embed.add_embed_field(
        name="👀 조회수",
        value=post["views"],
        inline=True,
    )

    embed.add_embed_field(
        name="🔢 게시번호",
        value=post["number"],
        inline=True,
    )

    embed.set_footer(
        text="KGEU Board Monitor"
    )

    embed.set_timestamp()

    webhook.add_embed(embed)

    response = webhook.execute()

    if response.status_code == 200:
        print("디스코드 전송 완료!")
    else:
        print(f"전송 실패 : {response.status_code}")