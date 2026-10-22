from django.apps import AppConfig
from django.db.models.signals import post_migrate

def criar_super_user_automatico(sender, **kwargs):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@exemplo.com', 'Admin12345')
        print("====== SUPERUSER ADMIN CRIADO COM SUCESSO ======")

class ConsultasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consultas'

    def ready(self):
        post_migrate.connect(criar_super_user_automatico, sender=self)