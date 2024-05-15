from django.core.mail import send_mail
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_mail_using_sendgrid(api_key, from_email, to_emails, subject, html_content):
    if api_key and from_email and to_emails:
        message = Mail(from_email=from_email, to_emails=to_emails, subject=subject, html_content=html_content)
        try:
            sg = SendGridAPIClient(api_key)
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)