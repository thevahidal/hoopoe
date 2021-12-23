from django.template.loader import render_to_string
from django.core.mail import get_connection, EmailMultiAlternatives

from django.conf import settings

def handle_send_email(organization, context, driver):
    
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
            to=[driver.username],
            connection=connection,
        )
        email.attach_alternative(html_message, "text/html")  # attach html version
        email.send()
