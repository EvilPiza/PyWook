from discord import Intents, Client, Message, File
from Bot_responses import get_response
import PyWook
import pyscreeze as pys
import Macro

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

    if 'start' in lowered:
        try:
            await message_.author.send("Starting Macro...") if is_private else await message_.channel.send("Starting Macro...")
        except Exception as e:
            print(e)
        Macro.__name__ = "__main__"       

    if 'exit' in lowered:
        try:
            await message_.author.send("Ending Macro...") if is_private else await message_.channel.send("Ending Macro...")
        except Exception as e:
            print(e)
        PyWook.start_macro_remotely = False
        PyWook.end_macro = True

    if 'image' in lowered:
        try:
            pys.screenshot(PyWook.image_path)
            await message_.author.send(file=File(fp=PyWook.image_path)) if is_private else await message_.channel.send(file=File(fp=PyWook.image_path))
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
    client.run(token=PyWook.discord_bot_token)


if __name__ == '__main__':
    main()
