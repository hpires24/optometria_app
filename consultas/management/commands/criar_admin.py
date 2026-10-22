from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Cria um super-utilizador automaticamente'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@exemplo.com', 'Secreta9703')
            self.stdout.write(self.style.SUCCESS('Administrador "admin" criado com sucesso!'))
        else:
            self.stdout.write(self.style.WARNING('O administrador "admin" já existe.'))