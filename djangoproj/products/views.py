from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Product
from .forms import RawProductForm, ProductForm


# def product_create_view(request):
#     form = RawProductForm()
#     if request.method == 'POST':
#         form = RawProductForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             Product.objects.create(**form.cleaned_data)
#         else:
#             print(form.errors)
#     return render(request,'product/product_create.html',{'form':form})


def product_create_view(request):
    initial_data = {'title':'My awesome title'}
    obj = Product.objects.get(id=1)
    form = ProductForm(request.POST or None,initial=initial_data,instance=obj)
    if form.is_valid():
        form.save()
        form = ProductForm()
    return render(request,'product/product_create.html',{'form':form})

def product_detail_view(request, id):
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    # obj = get_object_or_404(Product,id=id)
    return render(request,'product/detail.html',{'object':obj})

def product_delete_view(request,id):
    try:
        obj = Product.objects.get(id=id)
        obj.delete()
    except Product.DoesNotExist:
        raise Http404
    return HttpResponseRedirect('/')

def product_list_view(request):
    objects = Product.objects.all()
    return render(request,'product/product_list.html',{'products':objects})