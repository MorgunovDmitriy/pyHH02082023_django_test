from django.shortcuts import render, HttpResponse, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import ArticleNew
from django.views.generic import ListView, CreateView, UpdateView


def news_list(request):

    news = ArticleNew.objects.all()
    context = {"news": news}

    return render(request, 'news.html', context)

def news_detail(request, id):
    try:
        news_object = ArticleNew.objects.get(id=id)
    except ObjectDoesNotExist:
        return HttpResponse("Укажите верное id", status=404)
    context = {
        'news_object': news_object
    }
    return render(request, 'news_page.html', context)

class ArticleNewCreateView(CreateView):
    model = ArticleNew
    fields = '__all__'