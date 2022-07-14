from django.shortcuts import render
from django.views import View
# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, 'index.html')



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