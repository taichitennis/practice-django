from django.shortcuts import render
from django.http import HttpResponse
from .forms import FormA

def index(request):
    params = {
        'title': 'e class',
        'message': 'your data',
        'form': FormA()
    }
    if (request.method == 'POST'):
        params['message'] = 'Log in 中　<br>学籍番号：'+ request.POST['name']+'<br>学部：'+ request.POST['undergraduate']
        params['form']=FormA(request.POST)
    return render(request,'practice01/index.html',params)

# Create your views here.
