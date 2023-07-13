from telegram import Update
from telegram.ext import CallbackContext

from bot.buttons import btns
from bot.models import Log, User
from bot.questions import QUESTIONS, answers_A1, answers_A2, answers_B1, answers_B2, answers_C1, answers_C2


def start(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()

    if not tglog:
        tglog = Log()
        tglog.user_id = user.id
        tglog.save()
    log = tglog.messages

    if not tg_user:
        tg_user = User()
        tg_user.user_id = user.id
        tg_user.username = user.username
        tg_user.first_name = user.first_name
        tg_user.save()
        log['state'] = 1
        update.message.reply_html("Hello, welcome to the <b>Forward Academy</b>.\nEnter your name 🖊")
    else:
        if log['state'] >= 2:
            log.clear()
            log['state'] = 3
            update.message.reply_text("Click the button below to get the questions 👇", reply_markup=btns('menu'))

        else:
            log['state'] = 1
            update.message.reply_html("Hello, welcome to the <b>Forward Academy</b>.\nEnter your name 🖊")

    tglog.messages = log
    tglog.save()


def message_handler(update: Update, context: CallbackContext):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    log = tglog.messages
    tg_user = User.objects.filter(user_id=user.id).first()
    msg = update.message.text

    if log['state'] == 1:
        log['name'] = msg
        log['state'] = 2
        update.message.reply_text(
            'Send us your number by clicking the «Send number 📲» button',
            reply_markup=btns('contact')
        )
    if msg == "Start Test 📚":
        if log['state'] == 3:
            log['state'] = 4
            update.message.reply_html(QUESTIONS['A1'][1], reply_markup=btns("variant"))
            tg_user.total_score = 0

    elif log['state'] == 4:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A1_1 = msg
            if int(msg) == answers_A1[0]:
                tg_user.total_score += 1
            log['state'] = 5
            update.message.reply_html(QUESTIONS['A1'][2], reply_markup=btns("variant"))

    elif log['state'] == 5:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A1_2 = msg
            if int(msg) == answers_A1[1]:
                tg_user.total_score += 1
            log['state'] = 6
            update.message.reply_html(QUESTIONS['A1'][3], reply_markup=btns("variant"))

    elif log['state'] == 6:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A1_3 = msg
            if int(msg) == answers_A1[2]:
                tg_user.total_score += 1
            log['state'] = 7
            update.message.reply_html(QUESTIONS['A1'][4], reply_markup=btns("variant"))

    elif log['state'] == 7:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A1_4 = msg
            if int(msg) == answers_A1[3]:
                tg_user.total_score += 1
            log['state'] = 8
            update.message.reply_html(QUESTIONS['A1'][5], reply_markup=btns("variant"))
    elif log['state'] == 8:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A1_5 = msg
            if int(msg) == answers_A1[4]:
                tg_user.total_score += 1
            log['state'] = 9
            update.message.reply_html(QUESTIONS['A1'][6], reply_markup=btns("variant"))
    elif log['state'] == 9:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A1_6 = msg
            if int(msg) == answers_A1[5]:
                tg_user.total_score += 1
            log['state'] = 10
            update.message.reply_html(QUESTIONS['A1'][7], reply_markup=btns("variant"))
    elif log['state'] == 10:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A1_7 = msg
            if int(msg) == answers_A1[6]:
                tg_user.total_score += 1
            tg_user.save()
            tglog.save()
            if not tg_user.total_score >= 5:
                update.message.reply_html(f"Not bad 😉 Your English level is <b>A1</b>\n"
                                          "Start improving it with <a href='https://forwardacademy.uz/'>Forward Academy</a> !\n"
                                          , reply_markup=btns('menu'))
                log['state'] = 3
            else:
                log['state'] = 11
                update.message.reply_html("Good job 😃, keep going! Questions will get more difficult")
                update.message.reply_html(QUESTIONS['A2'][1], reply_markup=btns("variant"))
            tg_user.total_score = 0
    elif log['state'] == 11:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A2_1 = msg
            if int(msg) == answers_A2[0]:
                tg_user.total_score += 1
            log['state'] = 12
            update.message.reply_html(QUESTIONS['A2'][2], reply_markup=btns("variant"))

    elif log['state'] == 12:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A2_2 = msg
            if int(msg) == answers_A2[1]:
                tg_user.total_score += 1
            log['state'] = 13
            update.message.reply_html(QUESTIONS['A2'][3], reply_markup=btns("variant"))

    elif log['state'] == 13:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A2_3 = msg
            if int(msg) == answers_A2[2]:
                tg_user.total_score += 1
            log['state'] = 14
            update.message.reply_html(QUESTIONS['A2'][4], reply_markup=btns("variant"))

    elif log['state'] == 14:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A2_4 = msg
            if int(msg) == answers_A2[3]:
                tg_user.total_score += 1
            log['state'] = 15
            update.message.reply_html(QUESTIONS['A2'][5], reply_markup=btns("variant"))

    elif log['state'] == 15:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A2_5 = msg
            if int(msg) == answers_A2[4]:
                tg_user.total_score += 1
            log['state'] = 16
            update.message.reply_html(QUESTIONS['A2'][6], reply_markup=btns("variant"))

    elif log['state'] == 16:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A2_6 = msg
            if int(msg) == answers_A2[5]:
                tg_user.total_score += 1
            log['state'] = 17
            update.message.reply_html(QUESTIONS['A2'][7], reply_markup=btns("variant"))

    elif log['state'] == 17:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A2_7 = msg
            if int(msg) == answers_A2[6]:
                tg_user.total_score += 1
            log['state'] = 18
            update.message.reply_html(QUESTIONS['A2'][8], reply_markup=btns("variant"))

    elif log['state'] == 18:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.A2_8 = msg
            if int(msg) == answers_A2[7]:
                tg_user.total_score += 1
            if not tg_user.total_score >= 6:
                update.message.reply_html(f"Not bad 😉 Your English level is <b>A2</b>\n"
                                          "Start improving it with <a href='https://forwardacademy.uz/'>Forward Academy</a> !\n"
                                          , reply_markup=btns('menu'))
                log['state'] = 3
            else:
                log['state'] = 19
                update.message.reply_html("Good job 😃, keep going! Questions will get more difficult")
                update.message.reply_html(QUESTIONS['B1'][1], reply_markup=btns("variant"))
            tg_user.total_score = 0

    elif log['state'] == 19:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B1_1 = msg
            if int(msg) == answers_B1[0]:
                tg_user.total_score += 1
            log['state'] = 20
            update.message.reply_html(QUESTIONS['B1'][2], reply_markup=btns("variant"))

    elif log['state'] == 20:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B1_2 = msg
            if int(msg) == answers_B1[1]:
                tg_user.total_score += 1
            log['state'] = 21
            update.message.reply_html(QUESTIONS['B1'][3], reply_markup=btns("variant"))

    elif log['state'] == 21:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B1_3 = msg
            if int(msg) == answers_B1[2]:
                tg_user.total_score += 1
            log['state'] = 22
            update.message.reply_html(QUESTIONS['B1'][4], reply_markup=btns("variant"))

    elif log['state'] == 22:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B1_4 = msg
            if int(msg) == answers_B1[3]:
                tg_user.total_score += 1
            log['state'] = 23
            update.message.reply_html(QUESTIONS['B1'][5], reply_markup=btns("variant"))

    elif log['state'] == 23:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B1_5 = msg
            if int(msg) == answers_B1[4]:
                tg_user.total_score += 1
            log['state'] = 24
            update.message.reply_html(QUESTIONS['B1'][6], reply_markup=btns("variant"))

    elif log['state'] == 24:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B1_6 = msg
            if int(msg) == answers_B1[5]:
                tg_user.total_score += 1
            if not tg_user.total_score >= 4:
                update.message.reply_html(f"Not bad 😉 Your English level is <b>B1</b>\n"
                                          "Start improving it with <a href='https://forwardacademy.uz/'>Forward Academy</a> !\n"
                                          , reply_markup=btns('menu'))
                log['state'] = 3
            else:
                log['state'] = 25
                update.message.reply_html("Good job 😃, keep going! Questions will get more difficult")
                update.message.reply_html(QUESTIONS['B2'][1], reply_markup=btns("variant"))
            tg_user.total_score = 0

    elif log['state'] == 25:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B2_1 = msg
            if int(msg) == answers_B2[0]:
                tg_user.total_score += 1
            log['state'] = 27
            update.message.reply_html(QUESTIONS['B2'][2], reply_markup=btns("variant"))

    elif log['state'] == 27:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B2_2 = msg
            if int(msg) == answers_B2[1]:
                tg_user.total_score += 1
            log['state'] = 28
            update.message.reply_html(QUESTIONS['B2'][3], reply_markup=btns("variant"))

    elif log['state'] == 28:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B2_3 = msg
            if int(msg) == answers_B2[2]:
                tg_user.total_score += 1
            log['state'] = 29
            update.message.reply_html(QUESTIONS['B2'][4], reply_markup=btns("variant"))

    elif log['state'] == 29:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B2_4 = msg
            if int(msg) == answers_B2[3]:
                tg_user.total_score += 1
            log['state'] = 30
            update.message.reply_html(QUESTIONS['B2'][5], reply_markup=btns("variant"))

    elif log['state'] == 30:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B2_5 = msg
            if int(msg) == answers_B2[4]:
                tg_user.total_score += 1
            log['state'] = 31
            update.message.reply_html(QUESTIONS['B2'][6], reply_markup=btns("variant"))

    elif log['state'] == 31:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B2_6 = msg
            if int(msg) == answers_B2[5]:
                tg_user.total_score += 1
            log['state'] = 32
            update.message.reply_html(QUESTIONS['B2'][7], reply_markup=btns("variant"))

    elif log['state'] == 32:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.B2_7 = msg
            if int(msg) == answers_B2[6]:
                tg_user.total_score += 1
            if not tg_user.total_score >= 5:
                update.message.reply_html(f"Not bad 😉 Your English level is <b>B2</b>\n"
                                          "Start improving it with <a href='https://forwardacademy.uz/'>Forward Academy</a> !\n"
                                          , reply_markup=btns('menu'))
                log['state'] = 3
            else:
                log['state'] = 33
                update.message.reply_html("Good job 😃, keep going! Questions will get more difficult")
                update.message.reply_html(QUESTIONS['C1'][1], reply_markup=btns("variant"))
            tg_user.total_score = 0

    elif log['state'] == 33:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C1_1 = msg
            if int(msg) == answers_C1[0]:
                tg_user.total_score += 1
            log['state'] = 34
            update.message.reply_html(QUESTIONS['C1'][2], reply_markup=btns("variant"))

    elif log['state'] == 34:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C1_2 = msg
            if int(msg) == answers_C1[1]:
                tg_user.total_score += 1
            log['state'] = 35
            update.message.reply_html(QUESTIONS['C1'][3], reply_markup=btns("variant"))

    elif log['state'] == 35:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C1_3 = msg
            if int(msg) == answers_C1[2]:
                tg_user.total_score += 1
            log['state'] = 36
            update.message.reply_html(QUESTIONS['C1'][4], reply_markup=btns("variant"))

    elif log['state'] == 36:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C1_4 = msg
            if int(msg) == answers_C1[3]:
                tg_user.total_score += 1
            log['state'] = 37
            update.message.reply_html(QUESTIONS['C1'][5], reply_markup=btns("variant"))

    elif log['state'] == 37:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C1_5 = msg
            if int(msg) == answers_C1[4]:
                tg_user.total_score += 1
            log['state'] = 38
            update.message.reply_html(QUESTIONS['C1'][6], reply_markup=btns("variant"))

    elif log['state'] == 38:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C1_6 = msg
            if int(msg) == answers_C1[5]:
                tg_user.total_score += 1
            log['state'] = 39
            update.message.reply_html(QUESTIONS['C1'][7], reply_markup=btns("variant"))

    elif log['state'] == 39:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C1_7 = msg
            if int(msg) == answers_C1[6]:
                tg_user.total_score += 1
            if not tg_user.total_score >= 5:
                update.message.reply_html(f"Not bad 😉 Your English level is <b>C1</b>\n"
                                          "Start improving it with <a href='https://forwardacademy.uz/'>Forward Academy</a> !\n"
                                          , reply_markup=btns('menu'))
                log['state'] = 3
            else:
                log['state'] = 40
                update.message.reply_html("Good job 😃, keep going! Questions will get more difficult")
                update.message.reply_html(QUESTIONS['C2'][1], reply_markup=btns("variant"))
            tg_user.total_score = 0

    elif log['state'] == 40:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C2_1 = msg
            if int(msg) == answers_C2[0]:
                tg_user.total_score += 1
            log['state'] = 41
            update.message.reply_html(QUESTIONS['C2'][2], reply_markup=btns("variant"))

    elif log['state'] == 41:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C2_2 = msg
            if int(msg) == answers_C2[1]:
                tg_user.total_score += 1
            log['state'] = 42
            update.message.reply_html(QUESTIONS['C2'][3], reply_markup=btns("variant"))

    elif log['state'] == 42:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C2_3 = msg
            if int(msg) == answers_C2[2]:
                tg_user.total_score += 1
            log['state'] = 43
            update.message.reply_html(QUESTIONS['C2'][4], reply_markup=btns("variant"))

    elif log['state'] == 43:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C2_4 = msg
            if int(msg) == answers_C2[3]:
                tg_user.total_score += 1
            log['state'] = 44
            update.message.reply_html(QUESTIONS['C2'][5], reply_markup=btns("variant"))

    elif log['state'] == 44:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C2_5 = msg
            if int(msg) == answers_C2[4]:
                tg_user.total_score += 1
            log['state'] = 45
            update.message.reply_html(QUESTIONS['C2'][6], reply_markup=btns("variant"))

    elif log['state'] == 45:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C2_6 = msg
            if int(msg) == answers_C2[5]:
                tg_user.total_score += 1
            log['state'] = 46
            update.message.reply_html(QUESTIONS['C2'][7], reply_markup=btns("variant"))

    elif log['state'] == 46:
        if not msg.isdigit() or int(msg) not in [1, 2, 3, 4]:
            update.message.reply_text("Please select an existing answer option 🧐")
        else:
            tg_user.C2_7 = msg
            if int(msg) == answers_C2[6]:
                tg_user.total_score += 1
            if not tg_user.total_score >= 5:
                update.message.reply_html(f"Not bad 😉 Your English level is <b>C1</b>\n"
                                          "Start improving it with <a href='https://forwardacademy.uz/'>Forward Academy</a>\n"
                                          , reply_markup=btns('menu'))
            else:
                update.message.reply_html(f"<b>Congratulations</b> 🥳 You did exceptionally great."
                                          "Your English level is <b>C2</b>.\n"
                                          "However there is always a room for improvement. We are waiting for you in our education center\n<a href='https://forwardacademy.uz/'>Forward Academy</a> !"
                                          , reply_markup=btns('menu'))
            log['state'] = 3
            tg_user.total_score = 0
    tg_user.save()
    tglog.messages = log
    tglog.save()


def contact_handler(update, context):
    user = update.message.from_user
    tglog = Log.objects.filter(user_id=user.id).first()
    tg_user = User.objects.filter(user_id=user.id).first()
    log = tglog.messages
    contact = update.message.contact
    log['contact'] = contact.phone_number
    if log['state'] == 2:
        tg_user.name = log['name']
        log['state'] = 3
        tg_user.phone = log['contact']
        tg_user.save()
        update.message.reply_text("Your information has been saved ✅")
        update.message.reply_text("Click the button below to get the questions 👇", reply_markup=btns('menu'))

    tglog.messages = log
    tglog.save()
