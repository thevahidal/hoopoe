

from hoopoe.celery import app

from users.models import Driver, Organization

from core.utils import handle_send_email

@app.task
def handle_send_upupa(organization_id, context):
    organization = Organization.objects.get(id=organization_id)
    recipients = organization.recipients

    for recipient in recipients.all():
        drivers = recipient.drivers

        for driver in drivers.all():

            if driver.type == Driver.EMAIL:
               handle_send_email(organization, context, driver)