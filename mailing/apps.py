from time import sleep

from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mailing'

    # Переопределение для запуска периодической задачи
    def ready(self):
        from mailing.services import start
        sleep(2)
        start()
