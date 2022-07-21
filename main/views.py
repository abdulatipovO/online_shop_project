from django.shortcuts import render
from django.views import View
from .models import *
# Create your views here.

class HomePageView(View):
    def get(self, request):
        big_banner = Banner.objects.filter(banner_type='Big').order_by('-id')[:3]
        small_banners = Banner.objects.filter(banner_type='Small').order_by('-id')[:3]


        context = {
            "big_banner":big_banner,
            "small_banners":small_banners,
        }
        return render(request, 'index.html', context)



class ShopPageView(View):
    def get(self, request):
        return render(request, 'shop.html')



class DetailPageView(View):
    def get(self, request):
        return render(request, 'detail.html')



class ContactPageView(View):
    def get(self, request):
        return render(request, 'contact.html')


class CheckoutPageView(View):
    def get(self, request):
        return render(request, 'checkout.html')


class CartPageView(View):
    def get(self, request):
        return render(request, 'cart.html')