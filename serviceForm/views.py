from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from serviceForm.forms import CategoryForm, ServiceForm
from serviceForm.models import Category, Machine

from django.core import serializers
from django.views.generic import ListView, CreateView, UpdateView

# Create your views here.

#要有default pre-populated with initial values


def category(request):
    categories = Category.objects.all()
    return render(request, 'admin/category.html', {'categories': categories})


def categoryCreate(request):
    if request.method == 'GET':
        categoryForm = CategoryForm()
        return render(request, 'admin/categoryCreate.html', {'categoryForm': categoryForm})
    elif request.method == 'POST':
        categoryForm = CategoryForm(request.POST)
        if not categoryForm.is_valid():
            return render(request, 'admin/categoryCreate.html', {'categoryForm': categoryForm})
        categoryForm.save()
        messages.success(request, '新增成功')
        return redirect(reverse('serviceForm:category'))  # /serviceForm/category/


def categoryUpdate(request, categoryid):
    category = get_object_or_404(Category, categoryid=categoryid)  # Category.objects.get(categoryid=id)
    if request.method == 'GET':
        categoryForm = CategoryForm(instance=category)
        return render(request, 'admin/categoryUpdate.html', {'categoryForm': categoryForm})
    elif request.method == 'POST':
        categoryForm = CategoryForm(request.POST, instance=category)
        if not categoryForm.is_valid():
            return render(request, 'admin/categoryUpdate.html', {'categoryForm': categoryForm})
        categoryForm.save()
        messages.success(request, '修改成功')
        return redirect(reverse('serviceForm:category'))


def categoryDelete(request, categoryid):
    category = get_object_or_404(Category, categoryid=categoryid)
    if request.method == 'POST':
        category.delete()
        messages.success(request, '刪除成功')
    return redirect(reverse('serviceForm:category'))


def categoryRead(request, categoryid):
    category = get_object_or_404(Category, categoryid=categoryid)
    return render(request, 'admin/categoryRead.html', {'category': category})


def form(request):
    # return render(request, 'form.html')
    if request.method == 'GET':
        serviceForm = ServiceForm()
        return render(request, 'form.html', {'serviceForm': serviceForm})
    elif request.method == 'POST':
        serviceForm = ServiceForm(request.POST)
        # emplist =
        if not serviceForm.is_valid():
            return render(request, 'form.html', {'serviceForm': serviceForm})

        serviceForm.save()
        return redirect(reverse('serviceForm:form'))

def formarea(request):
    return render(request, 'formarea.html')


