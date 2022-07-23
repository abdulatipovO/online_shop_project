from .models import Card, CardProduct

class GetCard:
    def __init__(self,request) -> None:
        if request.session.get("card_id"):
            card = Card.objects.get(id=int(request.session.get("card_id")))
        else:
            card = Card.objects.create()
            request.session['card_id'] = card.id
        self.card = card
