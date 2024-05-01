from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.utils import timezone
from .models import Order, Product
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def view(request, client_id):
    # Получение всех заказов клиента за последние 7 дней
    orders_week = Order.objects.filter(client_id=client_id, order_date__gte=timezone.now() - timezone.timedelta(days=7))
    # Получение всех заказов клиента за последние 30 дней
    orders_month = Order.objects.filter(client_id=client_id, order_date__gte=timezone.now() - timezone.timedelta(days=30))
    # Получение всех заказов клиента за последний год
    orders_year = Order.objects.filter(client_id=client_id, order_date__gte=timezone.now() - timezone.timedelta(days=365))

    # Получение всех товаров из заказов за последние 7, 30 и 365 дней
    products_week = Product.objects.filter(order__in=orders_week).distinct()
    products_month = Product.objects.filter(order__in=orders_month).distinct()
    products_year = Product.objects.filter(order__in=orders_year).distinct()

    # Сортировка товаров по дате добавления
    products_week = products_week.order_by('-added_date')
    products_month = products_month.order_by('-added_date')
    products_year = products_year.order_by('-added_date')

    context = {
        'products_week': products_week,
        'products_month': products_month,
        'products_year': products_year,
    }

    return render(request, "myapp2/index.html", context)

def user_detail(request):
    if request.method == 'POST':
        client_id = request.POST.get('user_id')
        return redirect('index', client_id=client_id)
    else:
        return render(request, 'myapp2/Main.html')