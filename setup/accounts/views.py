from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from .forms import (
    UserProfileForm,
)

from countries_app.forms import TripForm

from .models import (
    UserProfile
)

from countries_app.models import (
    Trip
)

# Create your views here.
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('homepage')
    template_name = 'signup.html'

@login_required(login_url='login')
def profile_redirect(request):
    user = request.user
    if hasattr(user, 'profile'):
        return redirect('homepage')
    else:
        return redirect('create_profile')
    
@login_required(login_url='login')
def create_profile(request):
    user = request.user
    if (request.method == 'POST'):
        profile_form = UserProfileForm(request.POST)

        if (profile_form.is_valid()):
            print('Bom dia')
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            Trip(user=user, country=profile.country_origin).save()
            return redirect('homepage')

    form = UserProfileForm()
    context = {'form': form}
    return render(request, 'create_profile.html', context)

@login_required(login_url='login')
def profile(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    form = TripForm()
    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'profile.html', context)

@login_required(login_url='login')
def get_trips(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    trips = profile.user.trip.all()
    countries_list = list(map( lambda x: str(x), list(trips)))
    data = {
        'countries': countries_list
    }
    return JsonResponse(data)

@login_required(login_url='login')
def get_country_origin(request, profile_id):
    profile = UserProfile.objects.get(id=profile_id)
    origin = str(profile.country_origin)
    data = {
        'country': origin
    }
    return JsonResponse(data)