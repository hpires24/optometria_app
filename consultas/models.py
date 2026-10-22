from django.db import models
from django.utils import timezone

class Consulta(models.Model):
    data_consulta = models.DateField(default=timezone.now, verbose_name="Data da Consulta")
    nome_paciente = models.CharField(max_length=150, verbose_name="Nome do Paciente")
    lentes = models.BooleanField(default=False, verbose_name="Lentes de Contacto?")
    progressivas = models.BooleanField(default=False, verbose_name="Lentes Progressivas?")
    notas = models.TextField(blank=True, null=True, verbose_name="Notas")
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-data_consulta', '-criado_em']

    def __str__(self):
        return f"{self.nome_paciente} - {self.data_consulta.strftime('%d/%m/%Y')}"