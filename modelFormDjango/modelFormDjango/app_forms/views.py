from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  
from .forms import ClientForm
from .models import Client


def form_modelform(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente salvo com sucesso!")  
            return redirect('client_list')  
    else:
        form = ClientForm()

    context = {
        'form': form
    }
    return render(request, 'form_modelform.html', context=context)


def client_list(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'client_list.html', context=context)


def editar_cliente(request, id):
    cliente = get_object_or_404(Client, id=id)  
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado com sucesso!")
            return redirect('client_list')  
    else:
        form = ClientForm(instance=cliente)  

    context = {
        'form': form,
        'cliente': cliente
    }
    return render(request, 'edit.html', context=context)  

def excluir_cliente(request, id):
    cliente = get_object_or_404(Client, id=id)  
    if request.method == 'POST':  
        cliente.delete()
        messages.success(request, "Cliente excluído com sucesso!")
        return redirect('client_list')  
    
    context = {
        'cliente': cliente
    }
    return render(request, 'delete.html', context=context)
