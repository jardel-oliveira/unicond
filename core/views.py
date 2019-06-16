from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Morador
from .forms import dadosForm
from django.contrib import messages


def home(request):
    return render(request, 'core/home.html')



def nossosistema(request):
    return render(request, 'core/nossosistema.html')



def planos(request):
    return render(request, 'core/planos.html')



def login(request):
    return render(request, 'core/login.html')

def cadastro(request):
    return render(request, 'core/cadastro.html')

@login_required
def dashboard(request):
    dados = Morador.objects.all()
    return render(request, 'core/dashboard.html' , {'dados': dados})

@login_required
def dadosMorador(request, id):
    dadoid = get_object_or_404(Morador, pk=id)
    return render(request, 'core/morador.html', {'dadoid': dadoid})

@login_required
def novoMorador(request):
    form = dadosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('dashboard')

    return render(request, 'core/novomorador.html', {'form': form})


@login_required
def editMorador(request, id):
    edit = get_object_or_404(Morador, pk=id)
    form = dadosForm(instance=edit)

    if(request.method == 'POST'):
        form = dadosForm(request.POST, instance=edit)

        if(form.is_valid()):
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'core/editmorador.html', {'form': form, 'edit': edit})
    else:
        return render(request, 'core/editmorador.html', {'form': form, 'edit': edit})



@login_required
def deleteMorador(request, id):
    deletar = get_object_or_404(Morador, pk=id)
    deletar.delete()
    return redirect('dashboard')


    messages.info(request, 'Morador deletado com sucesso')