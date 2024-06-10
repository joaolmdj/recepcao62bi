from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from app.forms import VisitanteForm
from .models import Visitante
from .filters import VisitanteFilter
from django.core.paginator import Paginator
from datetime import date
from django.contrib import messages
import plotly.graph_objects as go
from plotly.offline import plot


@login_required
def visitantes(request):
    visitante = Visitante.objects.order_by('-data')
    filter = VisitanteFilter(request.GET, queryset=visitante)
    visitante = filter.qs

    today = date.today()
    d1 = today.strftime("%m/%Y")
    contexto = {
        'visitante': visitante,
        'filter': filter,
        'today': d1
    }


    return render(request, 'visitantes.html', contexto)


@login_required
def graficos(request):
    fusex = Visitante.objects.filter(secao__icontains ='Fusex')
    dentista = Visitante.objects.filter(secao__icontains='Dentista')
    medico = Visitante.objects.filter(secao__icontains='Medico')

    fusex = len(fusex)
    dentista = len(dentista)
    medico = len(medico)

    labels = 'Fusex', 'Medico', 'Dentista'
    sizes = [fusex, medico, dentista]
    cores = ["Green", "Olive", "Lime"]
    grafico = plot(go.Figure(data = go.Pie(labels=labels,values=sizes,marker_colors=cores)),output_type='div')

    context = {
        "grafico": grafico,
        "fusex": fusex,
        "dentista": dentista,
        "medico": medico
    }

    return render(request, 'graficos.html', context)


@login_required
def sobre(request):
    
    return render(request, 'sobre.html')


@login_required
def cadastro(request):
    form = VisitanteForm()
    table = Visitante.objects.all()

    if request.method == 'POST':
        formVisitante = VisitanteForm(request.POST or None)
        
        if formVisitante.is_valid():
            formVisitante.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return render(request, 'cadastro.html', {'form': form, 'table': table})
        else:
            return render(request, 'cadastro.html', {'form': formVisitante, 'table': table})

    context = {
        'form': form
    }

    return render(request, 'cadastro.html', context)


@login_required
def updateVisitante(request, id):
    obj = get_object_or_404(Visitante, id=id)
    delete = True
    form = VisitanteForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {
        'obj': obj,
        'form': form,
        'delete': delete
    }

    return render(request, 'cadastro.html', context)


@login_required
def deleteVisitante(request, id):
    obj = get_object_or_404(Visitante, id=id)
    obj.delete()

    return redirect('/')
