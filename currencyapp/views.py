from django.shortcuts import render
from forex_python.converter import CurrencyRates

api = CurrencyRates()


# def compare_currencies(cur1, cur2):
#     currency = api.get_rate(cur1, cur2)
#     return f'{cur1} to {cur2}: {currency:.3f}'


def convert_currency(cur1, cur2, price):
    count = api.convert(cur1, cur2, price)
    return f'{price} {cur1} to {cur2}: {count:.3f}'


# def compare(request):
#     if request.method == 'POST' and request.POST:
#         currency1 = request.POST['first_cur']
#         currency2 = request.POST['second_cur']
#         price = compare_currencies(currency1, currency2)
#         return render(request, 'currencyapp/currency_compare.html', {'price': price, 'title': 'Compare Currency'})
#     return render(request, 'currencyapp/currency_compare.html', {'title': 'Compare Currency'})


def convert(request):
    if request.method == 'POST' and request.POST:
        price = request.POST['price']
        currency1 = request.POST['first_cur']
        currency2 = request.POST['second_cur']
        convert_result = convert_currency(currency1, currency2, int(price))
        return render(request, 'currencyapp/convert_currency.html', {'convert_result': convert_result, 'title': 'Convert Currency'})
    return render(request, 'currencyapp/convert_currency.html', {'title': 'Convert Currency'})
