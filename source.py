from pyrogram import Client

API_ID = None  # int/str (https://my.telegram.org/app)
API_HASH = None  # str (https://my.telegram.org/app)

app = Client(
    "ClearfyBot",
    api_id=API_ID,
    api_hash=API_HASH,
)

TARGET = None  # Chat/Channel ID


async def main() -> None:
    async with app:
        async for message in app.search_messages(chat_id=TARGET, from_user="me"):
            await message.delete()
        return


if __name__ == "__main__":
    try:
        app.run(main())
    except KeyboardInterrupt:
        exit()

