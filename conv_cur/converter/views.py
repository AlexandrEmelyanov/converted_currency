import requests
from django.conf import settings
from django.shortcuts import render


def get_convert(request):
    response = requests.get(f'https://api.currencyapi.com/v3/latest?apikey={settings.API_KEY}').json()
    currencies = response.get('data')

    if request.method == 'POST':
        from_amount = request.POST.get('from-amount')
        if from_amount:
            from_curr = request.POST.get('from-curr')
            to_curr = request.POST.get('to-curr')

            converted_amount = round(currencies[to_curr]['value'] / currencies[from_curr]['value'] * float(from_amount), 2)

            context = {
                'from_curr': from_curr,
                'from_amount': from_amount,
                'to_curr': to_curr,
                'converted_amount': converted_amount,
                'currencies': currencies,
            }
            return render(request=request, template_name='converter/index.html', context=context)

    context = {'currencies': currencies}
    return render(request=request, template_name='converter/index.html', context=context)
