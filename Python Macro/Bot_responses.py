from random import randint

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return 'Well, you\'re awfully silent...'
    elif 'commands' in lowered:
        return 'I can tell you about me with "$who", you can roll dice with "$roll dice" and I can send images to you with "$image"!'
    elif 'roll dice' in lowered:
        return f'You rolled: {randint(1, 6)}'
    elif 'image' in lowered or 'start' in lowered or 'exit' in lowered:
        return ""
    elif 'version' in lowered:
        return "I am version 1.2!"
    elif 'who' in lowered:
        return """
        I am Py-Bot, a discord bot designed by EvilPiza on GitHub. My main purpose is to send images to you while your away from your PC!
        If I do anything incorrectly, PyWook is setup and if you're still are having issues contact me on GitHub or Discord! (@Bloxfriend590) (@EvilPiza)
                """
    else:
        return "I don't know what you just said."
