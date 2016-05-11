from django.shortcuts import render

def capture(request):
    return render(request, 'home.html',)
