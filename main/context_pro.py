from .models import Category
from card.models import Card
from card.card import GetCard

def get_category_objects(request):
    categorys = Category.objects.all()
    card_products_count = 0
    if request.session.get("card_id"):
        card =GetCard(request).card
        card_products_count = card.product.count()
        print(card_products_count)
        
    return {"categorys":categorys,
            "card_products_count":card_products_count
            }