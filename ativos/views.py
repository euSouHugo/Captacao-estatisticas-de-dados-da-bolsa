from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from ativos.utils import download_and_traform, filter_by_variation
from ativos.models import Ativo

class DashboardForm(forms.Form):
    volume = forms.DecimalField()
    ativo = forms.CharField()
    dataInicio = forms.CharField(required=False)
    dataFim = forms.CharField(required=False)
    variacao = forms.IntegerField()

@csrf_protect
def index(request):
    return render(request, "index.html")

@csrf_protect
def dashboard(request):
    error_message = ""
    if request.method == "POST":
        form = DashboardForm(request.POST)
        if form.is_valid():
            try:
                volume = float(form.cleaned_data['volume'])
                ativo = form.cleaned_data['ativo']
                data_inicio = form.cleaned_data['dataInicio']
                data_fim = form.cleaned_data['dataFim']
                variacao = form.cleaned_data['variacao']

                df = download_and_traform(ativo, data_inicio, data_fim)

                if df is not None:
                    media = df['Volume'].mean()
                    if media >= volume:
                        data_list = df.to_dict(orient='records')
                        total_rows = len(data_list)
                        result = filter_by_variation(df, variacao)
                        context = {"data_list": data_list, "total_rows": total_rows, "result": result}
                        return render(request, "dash.html", context)
                    else:
                        error_message = f"O volume médio do {ativo} é de {media}, não atende ao valor mínimo: {volume}"
                else:
                    error_message = f"Erro ao baixar dados para {ativo} entre {data_inicio} e {data_fim}"
            except ValueError:
                error_message = "O campo Volume deve ser um número válido."
        else:
            print(form.errors)  # Adicione esta linha
            error_message = "Por favor, corrija os erros no formulário."

        context = {"error_message": error_message}
        return render(request, "dash.html", context)
    else:
        # Se não for uma requisição POST, exiba o formulário vazio
        form = DashboardForm()
        return render(request, "dash.html", {"form": form})