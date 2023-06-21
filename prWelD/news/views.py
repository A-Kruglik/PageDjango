from django.shortcuts import render

def news_home(request):
    return render(request, 'news/news-home.html')

