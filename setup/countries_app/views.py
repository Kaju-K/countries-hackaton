from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db.models import Count

from .forms import (
    TripForm,
    CommentForm
)

from .models import (
    Trip,
    Comment,
    Country
)

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

@login_required(login_url='login')
def add_trip(request):
    if (request.method == "POST"):
        user = request.user
        trip_form = TripForm(request.POST)
        if (trip_form.is_valid()):
            trip = trip_form.save(commit=False)
            trip.user = user
            trip.save()
            return redirect('profile', user.profile.id)

@login_required(login_url='login')
def add_comment(request, country_id):
    if (request.method == "POST"):
        user = request.user
        comment_form = CommentForm(request.POST)
        if (comment_form.is_valid()):
            comment = comment_form.save(commit=False)
            comment.user = user
            comment.save()
            return redirect('trip', country_id)


@login_required(login_url='login')
def trip(request, country_id):
    country = Country.objects.get(id = country_id)
    trips = country.trip.all()
    comments = []
    for trip in trips:
        comment = trip.comment.all()
        if comment:
            comments.append(comment)
    user = request.user
    try:
        comment_form = CommentForm(initial={'trip': user.trip.get(country_id=country_id)})
    except:
        comment_form = "no"
    
    context = {
        'country': country,
        'country_id': country_id,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'trip/trips.html', context)

def search_country(request):
    if request.method == "POST":
        search_before = request.POST['search-bar']
        search_list = search_before.split(" ")
        for index, word in enumerate(search_list):
            if word.lower() not in ['of', 'and']:
                search_list[index] = word.title()
        search = " ".join(search_list)
        try:
            country_id = Country.objects.get(name=search).id
        except:
            return redirect('homepage')
        print(country_id)
        return redirect('trip', country_id)