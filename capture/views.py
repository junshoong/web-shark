from django.shortcuts import render

def capture(request):
    if(request.GET.get('capture')):
        print("capture!!")
    return render(request, 'home.html',)

