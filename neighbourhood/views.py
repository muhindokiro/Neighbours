from django.shortcuts import render,redirect,get_object_or_404
import datetime as dt
from .models import NeighbourHood,Post,Profile
from .email import send_welcome_email
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import NewNeighbourHoodForm,NewsLetterForm,RegisterForm,NewPostForm,NewProfileForm
from django.core.exceptions import ObjectDoesNotExist

# Create y views here.
# @login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'index.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    profile = Profile.profile()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            send_welcome_email(name,email)
            HttpResponseRedirect('profile')
    else:
        form = NewsLetterForm()
    return render(request, 'profile.html', {"profile":profile,"letterForm":form})

@login_required(login_url='/accounts/login/')
def home(request):
    neighbourhood = NeighbourHood.home()
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            send_welcome_email(name,email)
            HttpResponseRedirect('home')
    else:
        form = NewsLetterForm()
    return render(request, 'home.html', {"neighbourhood":neighbourhood,"letterForm":form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data['email']
            send_welcome_email(username,email)
            return redirect('index.html')
    else:
        form =RegisterForm()
    return render(request,'registration/registration_form.html',{'form':form})

@login_required(login_url='/accounts/login/')
def new_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewNeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            neighbourhood = form.save(commit=False)
            neighbourhood.save()
        return redirect('home','profile')
    else:
        form = NewNeighbourHoodForm()
    return render(request, 'new_hood.html', {"form": form})

@login_required(login_url='/accounts/login/')
def new_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('profile')
    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})

def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    # Returning the actual day of the week
    day = days[day_number]
    return day


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'neighbourhood' in request.GET and request.GET["neighbourhood"]:
        search_term = request.GET.get("neighbourhood")
        searched_neighbourhoods = NeighbourHood.search_by_neighbourhood_name(search_term)
        message = f"{search_term}"
        return render(request, 'search.html',{"message":message,"neighbourhoods": searched_neighbourhoods})
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def view(request):
    return render(request, 'view.html')

