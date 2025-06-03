from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse
from django.conf import settings
from django.views import View
import stripe


stripe.api_key = settings.STRIPE_SECRET_KEY


def index(request, *args, **kwargs):
    context = {
        # Puedes agregar datos dinámicos aquí si es necesario
    }
    return render(request, 'Donations/donations.html', context)


class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        amount = int(request.POST.get("amount", 1))  # en dólares
        if amount < 1:
            amount = 1

        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'mxn',
                    'product_data': {
                        'name': 'Donación',
                        
                    },
                    'unit_amount': amount * 100,  # Stripe usa centavos
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=request.build_absolute_uri('/donations/success/'),
            cancel_url=request.build_absolute_uri('/donations/cancel/'),
            locale='en',
        )
        return redirect(session.url, code=303)
    

def charge(request, *args, **kwargs):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST)
    return redirect(reverse('donations:success', args=[amount]))

def successMsg(request, *args, **kwargs):
    amount = args[0] if args else 0
    return render(request, 'Donations/success.html', {'amount': amount})


def cancelMsg(request):
    return render(request, 'Donations/cancel.html')