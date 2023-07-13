from django.core.management import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from quiz.settings import TOKEN
from bot.views import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        updater = Updater(TOKEN)

        updater.dispatcher.add_handler(CommandHandler('start', start))
        updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
        updater.dispatcher.add_handler(MessageHandler(Filters.contact, contact_handler))
        # updater.dispatcher.add_handler(MessageHandler(Filters.video, video_handler))
        # updater.dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

        updater.start_polling()
        updater.idle()