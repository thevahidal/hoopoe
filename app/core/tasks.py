from hoopoe.celery import app

from users.models import Driver, Organization

from core.drivers import db_driver, email_driver, telegram_driver


@app.task
def handle_send_upupa(organization_id, context):
    organization = Organization.objects.get(id=organization_id)
    recipients = organization.recipients

    for recipient in recipients.all():
        drivers = recipient.drivers

        for driver in drivers.all():
            if driver.type == Driver.EMAIL:
                email_driver(organization, context, driver)
            if driver.type == Driver.TELEGRAM:
                telegram_driver(organization, context, driver)


@app.task
def handle_store_upupa(organization_id, context):
    organization = Organization.objects.get(id=organization_id)
    db_driver(organization, context)