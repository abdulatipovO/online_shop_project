from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from .views import *

app_name = 'card'



urlpatterns = [
    path('', CardView.as_view(), name="card_view"),
    path('add', CardAddView.as_view(), name="card_add"),
]