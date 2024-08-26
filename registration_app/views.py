# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, DetailView
from .forms import ProfileForm, UserForm
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


#
def add_forTest_user(request):
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

    return render(request, 'user/add_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def add_demo_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST, request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data.get('password'))  # Hash the password
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('registration_app:all_user')
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    return render(request, 'user/add_demo_user.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


class EditUserView(UpdateView):
    template_name = 'user/edit_user.html'
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('registration_app:all_user')
    context_object_name = 'user'


class DeleteUserView(DeleteView):
    template_name = 'user/delete_user.html'
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('registration_app:all_user')


# class EditUserProfileView(UpdateView):
#     template_name = 'user/update.html'
#     model = User
#     # fields = '__all__'
#     form_class = UserForm
#     success_url = reverse_lazy('registration_app:edit_user')
#
#     # context_object_name = 'user'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_object(**kwargs)
#         pk = self.kwargs.get('pk')
#         context['user'] = Profile.objects.get(pk=pk)
#
#         return context


class Boss(TemplateView):
    template_name = 'boss/report.html'


class CustomPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'user/update.html'  # Change to your template path
    success_message = "Your password was successfully updated!"
    success_url = reverse_lazy(
        'registration_app:edit_user')  # Change 'profile' to the name of the view you want to redirect to after password change

    def get_object(self, queryset=None):
        # Get the user whose password we are changing based on the URL parameter
        return get_object_or_404(User, pk=self.kwargs['pk'])

    def get_form_kwargs(self):
        # Pass the user object to the form
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.get_object()
        return kwargs


class EditUserProfileView(UpdateView):
    model = Profile
    template_name = 'user/update.html'
    form_class = ProfileForm  # Assume you have a form for user updates
    success_url = reverse_lazy('registration_app:all_user')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # If you are trying to set some attribute for the user, do it like this:
        user = self.get_object()
        context['user'] = user
        # Example: if you want to update a user attribute, use dot notation
        # user.email = "newemail@example.com"  # This is how you set an attribute
        return context


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    model = Profile
    form_class = PasswordChangeForm
    template_name = 'user/profile.html'
    context_object_name = 'profile'

    def get_object(self):
        # Return the profile of the currently logged-in user
        return self.request.user.profile


def login_user(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('dashBoard_app:dashboard'))
    return render(request, 'login/loginOutlayer.html', context={'form': form})


@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "You are logged out")
    return HttpResponseRedirect(reverse('home'))



