from django.shortcuts import render, get_object_or_404
from .models import Hobby, PortfolioItem

def home(request):
    # Include context for additional customization
    return render(request, 'PortfolioDatabase/home.html', {
        'welcome_message': "Welcome to my portfolio!",
        'summary': "Hi, I'm a computer science student talking about my work and hobbies."
    })

def hobbies(request):
    hobbies_list = Hobby.objects.all()
    return render(request, 'PortfolioDatabase/hobbies.html', {'hobbies': hobbies_list})

def hobby_detail(request, hobby_id):
    hobby = get_object_or_404(Hobby, pk=hobby_id)
    return render(request, 'PortfolioDatabase/hobby_detail.html', {'hobby': hobby})

def portfolio(request):
    portfolio_items = PortfolioItem.objects.all()
    return render(request, 'PortfolioDatabase/portfolio.html', {'portfolio': portfolio_items})

def portfolio_detail(request, portfolio_id):
    portfolio_item = get_object_or_404(PortfolioItem, pk=portfolio_id)
    return render(request, 'PortfolioDatabase/portfolio_detail.html', {'portfolio_item': portfolio_item})

def contact(request):
    # Include context for additional customization
    return render(request, 'PortfolioDatabase/contact.html', {
        'email': "esmaeilmousavi@weber.edu"
    })

