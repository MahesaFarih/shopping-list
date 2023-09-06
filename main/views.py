from multiprocessing import context
from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Mahesa Farih Prasetyo',
        'class' : 'PBP B'
    }

    return render(request, "main.html", context)