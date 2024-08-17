from django.core.management import BaseCommand


from mailing.services import send_mailing, start


class Command(BaseCommand):
    """Кастомная команда для рассылки данных по почте"""

    def handle(self, *args, **options):
        """Соответственно метод для рассылки данных по почте"""
        # send_mailing()
        start()
