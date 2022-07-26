from .models import Card, CardProduct
from main.models import Product

class GetCard:
    def __init__(self,request) -> None:
        if request.session.get("card_id"):
            card = Card.objects.get(id=int(request.session.get("card_id")))
        else:
            card = Card.objects.create()
            request.session['card_id'] = card.id
        self.card = card
        self.request = request
    
    def getvalyut(self,product,qty):
        valyuta =self.request.session.get("valyuta", "usd")
        total_price = 0
        if valyuta=="usd":
            total_price = product.prise_usd * qty
        if valyuta=="uzs":
            total_price = product.prise_uzs * qty
        else:
            total_price = product.prise_rub * qty
        return total_price



    def add(self, product_id, qty=1):
        try:
            product = Product.objects.get(id=int(product_id))
        except:
            return {"status":"error","message":"Product does not exists", "card_total_products":self.card.product.count()}
        
        if self.card.product.filter(product=product).exists():
            return {"status":"error","message":"The product has been added to card", "card_total_products":self.card.product.count()}
        else:
            total_price = self.getvalyut(product, qty)
            card_product = self.card.product.create(qty=qty, product=product, total_price=total_price)
            self.card.calculated_summa += total_price
            self.card.total_summa += total_price
            self.card.save()
            return {"status":"ok","message":"The product added to  card" , "card_total_products":self.card.product.count()}

        
        