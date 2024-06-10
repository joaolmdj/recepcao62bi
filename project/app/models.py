from django.db import models
from django.utils import timezone
from datetime import datetime


SECAO_CHOICES = (
    ("Fusex", "Fusex"),
    ("Medico", "Medico"),
    ("Dentista", "Dentista"),
    ("SVP", "SVP"),
    ("Secretaria", "Secretaria"),
    ("Protocolo", "Protocolo"),
    ("SecMob", "SecMob"),
    ("SFPC", "SFPC"),
    ("Enfermaria", "Enfermaria"),
    ("Relações Publicas", "Relações Publicas")
)


def default_date():
    print(datetime.now)
    return datetime.now()


class Visitante(models.Model):
    nome = models.CharField('Nome', max_length=100)
    documento = models.CharField('Documento', max_length=20)
    secao = models.CharField('Seção', choices=SECAO_CHOICES, blank=False, null=False, max_length=50)
    data = models.DateTimeField(default=default_date)