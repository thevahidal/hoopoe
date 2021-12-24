import json

from django.template.loader import render_to_string
from django.core.mail import get_connection, EmailMultiAlternatives

from django.conf import settings

from decouple import config
import telegram


def email_driver(organization, context, driver):

    plain_version = "upupa_email_template.txt"
    html_version = "upupa_email_template.html"

    plain_message = render_to_string(
        plain_version,
        {
            **context,
        },
    )
    html_message = render_to_string(
        html_version,
        {
            **context,
        },
    )

    with get_connection(
        username=settings.EMAIL_UPUPA_USER,
        password=settings.EMAIL_UPUPA_PASSWORD,
    ) as connection:
        email = EmailMultiAlternatives(
            subject=f"{organization.name} | New Notification: {context.get('message')}",
            body=plain_message,
            from_email=settings.EMAIL_UPUPA_USER,
            to=[driver.account_id],
            connection=connection,
        )
        email.attach_alternative(html_message, "text/html")  # attach html version
        email.send()


def telegram_driver(organization, context, driver):
    try:
        bot = telegram.Bot(token=config("TELEGRAM_API_KEY"))
        bot.send_message(
            chat_id=driver.account_id,
            text=f"""
            **When**
            {context.get('timestamp')}
            **Message**
            {context.get('message')}
            **Info**
            {json.dumps(context.get('extra'), indent=4, sort_keys=True)}
            """,
        )
    except:
        print("Telegram driver failed.")
