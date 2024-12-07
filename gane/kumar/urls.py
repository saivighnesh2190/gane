from django.urls import path
from . import views
from django.urls import path
from .views import login

urlpatterns = [
    path('', views.first, name='home'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.account, name='account'),
    path('about-agr/', views.about_agr, name='about_agr'),
    path('contact/', views.contact, name='contact'),
    path('feedback/', views.feedback, name='feedback'),
    path('first/', views.first, name='first'),
    path('project/', views.project, name='project'),
    path('login/', views.login, name='login'),
    path('product/', views.product, name='product'),
    path('rating/', views.rating, name='rating'),
    path('about_section/', views.about_section, name='about_section'),
    path('climate/', views.climate, name='climate'),
    path('items/', views.items, name='items'),
    path('Fertilizer/', views.Fertilizer, name='Fertilizer'),
    path('Organic_seeds/', views.Organic_seeds, name='Organic_seeds'),
    path('Pesticide/', views.Pesticide, name='Pesticide'),
    path('Urea/', views.Urea, name='Urea'),
]