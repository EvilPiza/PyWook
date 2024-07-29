from discord import Intents, Client, Message, File
from Bot_responses import get_response
from PyWook import image_path as IMG_PATH, discord_bot_token as TOKEN
import pyscreeze as pys

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)


async def send_message(message_: Message, user_message: str) -> None:
    if not user_message:
        print('(Message is empty because intents were not enabled or code broke)')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]
    lowered = user_message.lower()
    if 'image' in lowered:
        try:
            pys.screenshot(IMG_PATH)
            await message_.author.send(file=File(fp=IMG_PATH)) if is_private else await message_.channel.send(file=File(fp=IMG_PATH))
        except Exception as e:
            print(e)
    if user_message[0] == "$":
        user_message = user_message[1:]
        try:
            response: str = get_response(user_message)
            await message_.author.send(response) if is_private else await message_.channel.send(response)
        except Exception as e:
            print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()
