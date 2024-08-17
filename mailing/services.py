from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django_apscheduler.models import DjangoJobExecution

# Импортирую свою почту
from dotenv import load_dotenv
import os

from mailing.models import Mailing

load_dotenv()


def send_mailing():
    # Получаю все рассылки
    mailings = Mailing.objects.all()
    # Запускаю цикл по рассылкам, где получаю данные и запускаю отправку сообщений
    for send_mail_for_customers in mailings:
        # Название рассылки
        subject_of_letter = send_mail_for_customers.message.subject_of_letter
        # Текст сообщения
        message = send_mail_for_customers.message.body_of_letter
        # Клиенты которым надо отправить сообщение
        mails = send_mail_for_customers.customers_of_service.all()
        # Отправляю рассылки
        for mailing in mails:
            send_mail(
                subject=subject_of_letter,
                message=message,
                from_email=os.getenv('mail'),
                recipient_list=[mailing]
            )


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_mailing(), 'interval', seconds=10)
    scheduler.start()
