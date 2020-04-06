from django.urls import path
from . import views


app_name = 'prod'
urlpatterns = [
    path('<int:id>', views.product_detail_view, name='product_detail'),
    path('create', views.product_create_view, name='product_create'),
    path('<int:id>/delete',views.product_delete_view, name='product_delete')
    ]