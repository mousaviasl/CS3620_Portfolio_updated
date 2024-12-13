from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('hobbies/', views.hobbies, name='hobbies'),
    path('hobbies/<int:hobby_id>/', views.hobby_detail, name='hobby_detail'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<int:portfolio_id>/', views.portfolio_detail, name='portfolio_detail'),
    path('contact/', views.contact, name='contact'),
]