from django.shortcuts import render, redirect
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

    consultas = Consulta.objects.all()[:10]  # Obtém as 10 consultas mais recentes
    return render(request, 'consultas/home.html', {'form': form, 'consultas': consultas})