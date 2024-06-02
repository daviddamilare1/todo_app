from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic













                # AUTHENTICATION



        # Registration
class Registration (generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy ('login')


         # LogOut
def logout_view(request):
    logout(request)
    return redirect ('login')