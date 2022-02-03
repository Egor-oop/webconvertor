from django.urls import path

from currencyapp.views import convert, crypto, currency

urlpatterns = [
    path('', currency, name='currency'),
    path('crypto/', crypto, name='crypto_convert'),
    path('convert/', convert, name='cur_convert'),
]
