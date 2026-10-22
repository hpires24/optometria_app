from django.shortcuts import render, redirect, get_object_or_404
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

    consultas = Consulta.objects.all()[:20]  # Mostra as últimas 20 consultas
    return render(request, 'consultas/home.html', {'form': form, 'consultas': consultas})

def eliminar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    consulta.delete()
    return redirect('home')