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
        add_status = card.add(product_id)
        return JsonResponse({"status":add_status['message'] ,"card_total_products":add_status['card_total_products']})