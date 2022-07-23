from django.urls import path,include
from .views import *
app_name = "main"

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('shop', ShopPageView.as_view(), name="shop"),
    path('detail', DetailPageView.as_view(), name="detail"),
    path('contact', ContactPageView.as_view(), name="contact"),
    path('checkout', CheckoutPageView.as_view(), name="checkout"),
    # path('cart', CartPageView.as_view(), name="cart"),

]