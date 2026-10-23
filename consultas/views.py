from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Consulta
from .forms import ConsultaForm

def home(request):
    if request.method == 'POST':
        form = ConsultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ConsultaForm()

    consultas_list = Consulta.objects.all().order_by('-data_consulta')

    paginator = Paginator(consultas_list, 20)
    page_number = request.GET.get('page')
    consultas = paginator.get_page(page_number)

    return render(request, 'consultas/home.html', {
        'form': form,
        'consultas': consultas,
        'total_consultas': paginator.count
    })

def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        form = ConsultaForm(request.POST, instance=consulta)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ConsultaForm(instance=consulta)

    return render(request, 'consultas/editar.html', {'form': form, 'consulta': consulta})

def eliminar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.delete()
    return redirect('home')