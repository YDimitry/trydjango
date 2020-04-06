from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    # path('',views.article_list, name='article_list'),
    # path('<int:id>', views.article_detail, name='article_detail')
    path('',views.ArticleListView.as_view(), name='article_list'),
    path('<int:id>',views.ArticleDetailView.as_view(), name='article_detail'),
    path('create',views.ArcitleCreateView.as_view(), name='article_create'),
    path('<int:id>/update',views.ArticleUpdateView.as_view(), name='article_update'),
    path('<int:id>/delete',views.ArticleDeleteView.as_view(), name='article_delete')

]