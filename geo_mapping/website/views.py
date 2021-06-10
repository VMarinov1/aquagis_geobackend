from django.shortcuts import render

def home(request):
    obj = {
        #'title': None,
        #'content': None
    }
    return render(request, 'website/main.html', obj)

