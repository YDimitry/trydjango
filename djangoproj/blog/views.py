from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from .models import Article
from . import forms

from django.views.generic import (
CreateView,
DetailView,
ListView,
UpdateView,
DeleteView
)
class ArcitleCreateView(CreateView):
    template_name = 'article_create.html'
    form_class = forms.ArticleForm
    queryset = Article.objects.all()
    # success_url = 'article'
    def get_success_url(self):
        return '/article'

class ArticleUpdateView(UpdateView):
    template_name = 'article_create.html'
    form_class = forms.ArticleForm
    # queryset = Article.objects.all()

    def get_success_url(self):
        return reverse('article:article_list')

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)

class ArticleDeleteView(DeleteView):
    template_name = 'article_delete.html'

    def get_success_url(self):
        return reverse('article:article_list')

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)

class ArticleObjectMixin:
    model = Article
    lookup = 'id'
    def get_object(self):
        id = self.kwargs.get(self.lookup)
        obj = None
        if id:
            obj = get_object_or_404(self.model,id=id)
        return obj

class ArticleListView(View):
    template_name = 'article_list.html'
    queryset = Article.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self,request,*args,**kwargs):
        return render(request,self.template_name,{'object_list':self.get_queryset()})

class ArticleDetailView(DetailView):
    template_name = 'article_detail.html'
    # queryset = Article.objects.all()
    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Article,id=id_)
# def article_list(request):
#     objects = Article.objects.all()
#     return render(request,'article_list.html',{'articles':objects})
#
# def article_detail(request,id):
#     try:
#         obj = Article.objects.get(id=id)
#     except Article.DoesNotExist:
#         raise Http404
#     return render(request, 'article_detail.html', {'article': obj})