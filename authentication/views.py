from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from django.views.generic import View

from authentication import forms
from authentication.forms import LoginForm


class LoginPage(View):
    form_class = forms.LoginForm
    template_name = 'authentication/login.html'

    def get(self, request):
        form = self.form_class()
        message = ''
        context = {
            "form": form,
            "message": message}

        return render(request, self.template_name,  context)

    def post(self, request):
        form = self.form_class(request.POST)
        message = ''
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                #message = f"Bonjour {user.username} ! Vous êtes connecté"
                return redirect('home')
            else:
                message = 'Idendentifiants invalides'

        context = {
            "form": form,
            "message": message}

        return render(request, self.template_name, context)



def login_page(request):
    form = LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                #message = f"Bonjour {user.username} ! Vous êtes connecté"
                return redirect('home')
            else:
                message = 'Idendentifiants invalides'

    context = {
        "form": form,
        "message": message}

    return render(request, 'authentication/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('login')


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentication/signup.html', context={'form': form})


def upload_profile_photo(request):
    form = forms.UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = forms.UploadProfilePhotoForm(
            request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'authentication/upload_profile_photo.html', context={'form': form})
