from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from users.models import CustomUser


class Command(BaseCommand):
    help = 'Creating superuser & few users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Number of creating users')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        user_data = input('Enter your name: ')
        random_string = get_random_string(6)
        CustomUser.objects.create_superuser(
            username=random_string, email=f"{random_string}@gmail.com", password='123')

        for i in range(total):
            random_string = get_random_string(6)
            CustomUser.objects.create_user(
                username=random_string, email=f'{random_string}@gmail.com', password='123')
