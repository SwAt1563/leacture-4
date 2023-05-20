from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponseRedirect, reverse
from .forms import RegistrationForm, LoginForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home:index'))
    else:
        form = RegistrationForm()

    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    pass



def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to a success page
                return HttpResponseRedirect(reverse('home:index'))
            else:
                # Invalid credentials
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()

    return render(request, 'account/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:index'))


