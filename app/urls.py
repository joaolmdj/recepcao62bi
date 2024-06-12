from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.visitantes),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cadastro/', views.cadastro),
    path('graficos/', views.graficos),
    path('sobre/', views.sobre),
    path('visitante/<id>/update', views.updatevisitante, name='updateVisitante'),
    path('visitante/<id>/delete', views.deletevisitante, name='deleteVisitante'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )