from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from .card import GetCard
# Create your views here.



class CardView(View):
    def get(self, request):
        return render(request, "cart.html")


class CardAddView(View):
    def get(self, request):
        product_id = request.GET.get('product_id')
        card =GetCard(request)
        print()
        print(product_id)
        print()
        return JsonResponse({"status":"Qabul qilindi"})