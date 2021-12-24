from django.core.management.base import BaseCommand, CommandError

from telegram.ext import CallbackContext, Updater, CommandHandler
from telegram import Update
from decouple import config

from users.models import Driver, OrganizationAPIKey, Recipient

ARGS_ERROR_TEXT = "After /init, you need to provide your recipient username and the API key. e.g. /init 12344 h00p0e_ap1_key"


def init(update: Update, context: CallbackContext):
    if len(context.args) == 2:
        recipient_username, key = context.args
    else:
        context.bot.send_message(chat_id=update.effective_chat.id, text=ARGS_ERROR_TEXT)
        return

    if recipient_username == "" or key == "":
        context.bot.send_message(chat_id=update.effective_chat.id, text=ARGS_ERROR_TEXT)
        return

    else:
        try:
            api_key = OrganizationAPIKey.objects.get_from_key(key)
            organization = api_key.organization
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="API key is not valid or expired. Try again.",
            )
            return

        try:
            recipient = Recipient.objects.get(
                organization=organization, username=recipient_username
            )
        except:
            context.bot.send_message(
                chat_id=update.effective_chat.id,
                text="Recipient username is not valid.",
            )
            return

        Driver.objects.create(
            recipient=recipient,
            type=Driver.TELEGRAM,
            account_id=update.effective_chat.id,
        )

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Your account successfully subscribed to the Telegram driver.",
        )
        return


    
TELEGRAM_API_KEY = config("TELEGRAM_API_KEY", None)

class Command(BaseCommand):
    help = "Initialize telegram client."

    def handle(self, *args, **kwargs):
        try:
            if TELEGRAM_API_KEY:
                updater = Updater(token=TELEGRAM_API_KEY, use_context=True)
                dispatcher = updater.dispatcher

                init_handler = CommandHandler("init", init)
                dispatcher.add_handler(init_handler)

                updater.start_polling()
                print("Telegram client polling started...")

                updater.idle()

            else:
                print("Telgram API key is required for using Telegram driver.")
        except:
            raise CommandError("Telegram client initialization failed.")
