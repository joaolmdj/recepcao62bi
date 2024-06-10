import django_filters
from .models import Visitante


class VisitanteFilter(django_filters.FilterSet):
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
    secao = django_filters.ChoiceFilter(label="Seção", choices=SECAO_CHOICES)
    nome = django_filters.CharFilter(lookup_expr='icontains')
    documento = django_filters.CharFilter(lookup_expr='icontains')

    

    class Meta:
        model = Visitante

        fields = {
            "nome": ["icontains"],
            "documento": ["icontains"],
        }
