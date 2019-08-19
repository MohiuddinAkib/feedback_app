import os
import smtplib
from email.mime.text import MIMEText


def send_mail(customer, dealer, rating, comments):
    port = os.environ.get('MAIL_PORT')
    host = os.environ.get('MAIL_HOST')
    sender = f"Private Person <{os.environ.get('MAIL_SENDER')}>"
    receiver = f"A Test User <{os.environ.get('MAIL_RECIEVER')}>"
    username = os.environ.get('MAIL_USER')
    password = os.environ.get('MAIL_PASSWORD')

    message = f"""\
    <h3>New feedback submission</h3>.
    <ul>
        <li>Customer: {customer}</li>
        <li>Dealer: {dealer}</li>
        <li>Rating: {rating}</li>
        <li>Comments: {comments}</li>
    </ul>"""

    msg = MIMEText(message, 'html')
    msg['Subject'] = "Feedback"
    msg['From'] = sender
    msg['To'] = receiver

    with smtplib.SMTP(host, port) as server:
        server.login(username,
                     password)
        server.sendmail(sender, receiver, msg.as_string())
