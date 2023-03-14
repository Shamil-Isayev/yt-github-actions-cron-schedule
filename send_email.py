import smtplib
import ssl
import os


port = 465
smtp_server = "smtp.gmail.com"
SENDER_EMAIL = os.environ.get('USER_EMAIL')
SENDER_PASSWORD = os.environ.get('USER_PASSWORD')
RECIPIENT_EMAIL = os.environ.get('RECIPIE_EMAIL')
message = """\
Subject: GitHub Email Report

This is your daily email report.
"""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(SENDER_EMAIL, SENDER_PASSWORD)
    server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, message)