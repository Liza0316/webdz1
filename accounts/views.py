from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages 
from django.contrib.auth import login 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomUserCreationForm, CustomUserChangeForm

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('/products/') 
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/products/') 
    
@login_required 
def profile_edit(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваш профіль було успішно оновлено!')
            return redirect('/products/') 
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'registration/profile_edit.html', {
        'form': form
    })

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'