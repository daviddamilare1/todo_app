from django.urls import path
from members import views









urlpatterns = [
    
    path('register/', views.Registration.as_view(), name= 'register'),
    path ('account/logout', views.logout_view, name = 'logout_view'),
]