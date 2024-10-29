# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)  # Log the user in after registration
            messages.success(request, 'Your account has been created!')
            return redirect('home')  # Redirect to home or another page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        return redirect('create-profile')  # or another appropriate action

    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'users/profile.html', context)

@login_required
def create_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile if hasattr(request.user, 'profile') else None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user  # Associate the profile with the current user
            profile.save()
            messages.success(request, 'Your profile has been created!')
            return redirect('profile')  # Redirect to the profile page after saving
    else:
        form = ProfileUpdateForm(instance=request.user.profile if hasattr(request.user, 'profile') else None)
    
    return render(request, 'create_profile.html', {'form': form})

@login_required
def custom_logout(request):
    auth_logout(request)
    return render(request, 'users/logout.html', {})

def test_view(request):
    if request.user.is_authenticated:
        return HttpResponse("User is authenticated")
    else:
        return HttpResponse("User is not authenticated")
