from telegram import ReplyKeyboardMarkup, KeyboardButton


def btns(type=None):
    btn = []
    if type == 'menu':
        btn = [
            [KeyboardButton("Start Test 📚")],
        ]

    elif type == 'contact':
        btn = [
            [KeyboardButton("«Send number 📲»", request_contact=True)]
        ]

    elif type == "variant":
        btn = [[
            KeyboardButton("1"),
            KeyboardButton("2"),
            KeyboardButton("3"),
            KeyboardButton("4"),

        ]]

    return ReplyKeyboardMarkup(btn, resize_keyboard=True)

