# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from registration_app.models import Profile


def add_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User has been added successfully!")
            return redirect('registration_app:all_user')
    else:
        form = UserCreationForm()
    return render(request, 'user/add_user.html', {'form': form})


# views.py

def all_user(request):
    users = User.objects.all()
    return render(request, 'user/all_user.html', {'users': users})


class CreateUserView(CreateView):
    template_name = 'user/add_demo_user.html'
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('registration_app:all_user')


from .forms import ProfileForm, UserForm


def create_same_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('registration_app:all_user')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'user/same_add_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
