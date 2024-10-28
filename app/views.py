from django.shortcuts import render
from .models import Produto

def index(request):
    produtos = Produto.objects.all()
    context ={
        'curso':'Jota Personalizados',
        'descricao':'Presenteie quem voce ama!',
        'produtos': produtos,
    }
    return render(request,'index.html',context)
    

def contato(request):
    return render(request,'contato.html')

def produto(request,pk):
    produtos = Produto.objects.get(pk=pk)
    context = {
        'produtos':produtos,
    }
    return render(request,'produto.html',context)

