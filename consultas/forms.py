from django import forms
from .models import Consulta

class ConsultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['data_consulta', 'nome_paciente', 'lentes', 'progressivas','notas']
        widgets = {
            'data_consulta': forms.DateInput(attrs={'type': 'date', 'class': 'w-full p-3 border border-gray-300 rounded-lg text-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'}),
            'nome_paciente': forms.TextInput(attrs={'placeholder': 'Ex: Maria Silva', 'class': 'w-full p-3 border border-gray-300 rounded-lg text-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'}),
            'lentes': forms.CheckboxInput(attrs={'class': 'w-6 h-6 text-blue-600 rounded border-gray-300 focus:ring-blue-500'}),
            'progressivas': forms.CheckboxInput(attrs={'class': 'w-6 h-6 text-blue-600 rounded border-gray-300 focus:ring-blue-500'}),
            'notas': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Observações rápidas...', 'class': 'w-full p-3 border border-gray-300 rounded-lg text-lg focus:ring-2 focus:ring-blue-500 focus:outline-none'}),
        }