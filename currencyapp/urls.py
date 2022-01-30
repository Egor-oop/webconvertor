from django.urls import path

from currencyapp.views import convert

urlpatterns = [
    # path('compare/', compare, name='cur_compare'),
    path('convert/', convert, name='cur_convert'),
]
