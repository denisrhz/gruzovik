
from django.shortcuts import render, redirect
from .models import *
from .forms import *

def fast(request):
	services = Services.objects.all()
	return render(request, 'basesite/fast.html', context={'services': services})

def home(request):
	services = Services.objects.all()
	return render(request, 'basesite/home.html', context={'services': services})

def services(request, slug):
	services = Services.objects.all()
	service = Services.objects.get(slug__iexact=slug)
	return render(request, 'basesite/service.html', context={'service': service, 'services': services})

def vacancy(request):
	services = Services.objects.all()
	vacancys = Vacancy.objects.all()
	return render(request, 'basesite/vacancy.html', context={'vacancys': vacancys, 'services': services})

def vacancy_detail(request, pk):
	services = Services.objects.all()
	vacancy = Vacancy.objects.get(pk=pk)
	return render(request, 'basesite/vacancy_detail.html', context={'vacancy': vacancy, 'services': services})

def stock(request):
	services = Services.objects.all()
	return render(request, 'basesite/stock.html', context={'services': services})

def reviews(request):
	services = Services.objects.all()
	reviews = Reviews.objects.all()
	if request.method == "POST":
		form = ReviewsForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
	else:
		form = ReviewsForm()
	return render(request, 'basesite/reviews.html', context={'services': services, 'reviews': reviews, 'form': form})

	

def contacts(request):
	services = Services.objects.all()
	return render(request, 'basesite/contacts.html', context={'services': services})

		