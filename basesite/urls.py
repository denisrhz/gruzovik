from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name='home_url'),
	path('services/<str:slug>/', services, name='services_detail_url'),
	path('vacancy/', vacancy, name='vacancy_url'),
	path('vacancy/<int:pk>/', vacancy_detail, name='vacancy_detail_url'),
	path('stock/', stock, name='stock_url'),
	path('reviews/', reviews, name='reviews_url'),
	path('contacts/', contacts, name='contacts_url'),
	path('fast/', fast, name='fast_url'),
]