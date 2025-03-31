from flask_mail import Message
from src import mail
from flask import current_app

def send_email(subject, recipient, body):
    msg = Message(subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[recipient])
    msg.body = body
    mail.send(msg)
