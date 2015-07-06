# -*- coding: utf-8 -*-
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import ModelForm
from django.views.generic import UpdateView, DeleteView
from .models import Product

# Create your views here.

def home(request):
    return render(request, 'products/index.html', {})

def products_list(request):
    products = Product.objects.all()

    # try to order products list
    order_by = request.GET.get('order_by', '')
    if order_by in ('first_name', 'description', 'price'):
        products = products.order_by(order_by)
        if request.GET.get('reverse', '') == '1':
            products = products.reverse()

    # paginate students
    paginator = Paginator(products, 4)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        products = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver
        # last page of results.
        products = paginator.page(paginator.num_pages)

    return render(request, 'products/products_list.html', {'products': products})


def products_add(request):
    # was form posted?
    if request.method == "POST":
        # was form add button clicked?
        if request.POST.get('add_button') is not None:
            # errors collection
            errors = {}

            # data for product object
            data = {'modified_at': request.POST.get('modified_at')}
            # data = {'middle_name': request.POST.get('middle_name'),
            #     'notes': request.POST.get('notes')}

            # validate user input
            first_name = request.POST.get('first_name', '').strip()
            if not first_name:
                errors['first_name'] = u"Назва є обов'язковим"
            else:
                data['first_name'] = first_name

            slug = request.POST.get('slug', '').strip()
            if not slug:
                errors['slug'] = u"Назва-мітка є обов'язковим"
            else:
                data['slug'] = slug

            description = request.POST.get('description', '').strip()
            if not description:
                errors['description'] = u"Опис є обов'язковим"
            else:
                data['description'] = slug

            created_at = request.POST.get('created_at', '').strip()
            if not created_at:
                errors['created_at'] = u"Дата створення"
            else:
                try:
                    datetime.strptime(created_at, '%Y-%m-%d')
                except Exception:
                    errors['created_at'] = u"Введіть коректний формат дати (Напр. 2015-07-06)"
                else:
                    data['created_at'] = created_at

            price = request.POST.get('price', '').strip()
            if not price:
                errors['price'] = u"Ціна  є обов'язкова"
            else:
                data['price'] = price

            # save product
            if not errors:
                product = Product(**data)
                product.save()

                # redirect to products list
                return HttpResponseRedirect(
                    u'%s?status_message=Продукт успішно додано!' % reverse('products'))
            else:
                # render form with errors and previous user input
                return render(request, 'products/products_add.html',
                              {'product': Product.objects.all().order_by('first_name'), 'errors': errors})
        elif request.POST.get('cancel_button') is not None:
            # redirect to home page on cancel button
            return HttpResponseRedirect(
                u'%s?status_message=Додавання Продукта скасовано!' % reverse('products'))
    else:
        # initial form render

        return render(request, 'products/products_add.html', {'products':Product.objects.all().order_by('first_name')})


class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'products/products_edit.html'
    fields = ['first_name', 'slug', 'description', 'price', 'created_at', 'modified_at']

    def get_success_url(self):
        return u'%s?status_message=Продукт успішно збережено!' % reverse('products')

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(
                u'%s?status_message=Редагування продукта відмінено!' % reverse('products'))
        else:
            return super(ProductUpdateView, self).post(request, *args, **kwargs)

# def products_delete(request):
#     return HttpResponse(<p>'delete product'</p>)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/products_confirm_delete.html'

    def get_success_url(self):
        return u'%s?status_message=Продукт успішно видалено!' \
            % reverse('products')

    # def post(self, request, *args, **kwargs):
    #     if request.POST.get('cancel_button'):
    #         return HttpResponseRedirect(
    #             u'%s?status_message=Видалення продукта відмінено!' % reverse('products'))
    #     else:
    #         return super(ProductUpdateView, self).post(request, *args, **kwargs)