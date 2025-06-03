from django.urls import path
from . import views

app_name="donations"

urlpatterns = [
    #path('', DonateView.as_view(), name='donations'),
    path('', views.index, name="donations"),
    path('charge/', views.charge, name="charge"),
    path('create-checkout-session/', views.CreateCheckoutSessionView.as_view(), name='create_checkout_session'),
    path('success/', views.successMsg, name='success'),
    path('cancel/', views.cancelMsg, name='cancel'),
]