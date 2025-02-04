from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),  # Login page as the default page
    path('home/', views.home, name='home'),  # Home page
    path('option1/', views.option1, name='option1'),
    path('option2/', views.option2, name='option2'),
    path('option3/', views.option3, name='option3'),
    path('option4/', views.option4, name='option4'),
    path('option5/', views.option5, name='option5'),
]
