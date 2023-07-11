from django.shortcuts import render


def index(request):
    data = {
        'title': 'Добро пожаловать!',
        'values': ['Some', 'Hello']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about-us.html')

def contact(request):
    return render(request, 'main/contact.html')
