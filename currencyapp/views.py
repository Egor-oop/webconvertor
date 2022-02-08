from django.shortcuts import render
from forex_python.converter import CurrencyRates

import requests
import json

api = CurrencyRates()


def crypto_currency(cur):
    url_all = 'https://api.bittrex.com/api/v1.1/public/getcurrencies'

    j = requests.get(url_all)
    data = json.loads(j.text)
    crypto = cur

    cur_url = f'https://api.bittrex.com/api/v1.1/public/getticker?market=USD-{crypto}'
    j = requests.get(cur_url)
    data = json.loads(j.text)
    price = data['result']['Ask']
    return f'{crypto} in USD: {price}'


def convert_currency(cur1, cur2, price):
    count = api.convert(cur1, cur2, price)
    return f'{price} {cur1} to {cur2}: {count:.3f}'


def currency(request):
    return render(request, 'currencyapp/currency.html', {'title': 'Currency'})


def crypto(request):
    if request.method == 'POST' and request.POST:
        currency = request.POST['crypto_cur']
        price = crypto_currency(currency)
        return render(request, 'currencyapp/crypto_compare.html', {'price': price, 'title': 'Crypto Currency'})
    return render(request, 'currencyapp/crypto_compare.html', {'title': 'Crypto Currency'})


def convert(request):
    if request.method == 'POST' and request.POST:
        price = request.POST['price']
        currency1 = request.POST['first_cur']
        currency2 = request.POST['second_cur']
        convert_result = convert_currency(currency1, currency2, float(price))
        return render(request, 'currencyapp/convert_currency.html',
                      {'convert_result': convert_result, 'title': 'Convert Currency'})
    return render(request, 'currencyapp/convert_currency.html', {'title': 'Convert Currency'})
