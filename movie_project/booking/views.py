from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Movie, Seat, Booking
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('welcome')
        else:
            messages.error(request, "Invalid credentials")
    return render(request, 'index.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def welcome_view(request):
    return render(request, 'welcome.html')

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {'movies': movies})

def movie_detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    seats = Seat.objects.filter(is_booked=False)
    return render(request, 'movie_detail.html', {'movie': movie, 'seats': seats})

def book_seat(request, movie_id, seat_id):
    if not request.user.is_authenticated:
        return redirect('login')
    movie = Movie.objects.get(id=movie_id)
    seat = Seat.objects.get(id=seat_id)
    seat.is_booked = True
    seat.save()
    Booking.objects.create(user=request.user, movie=movie, seat=seat)
    return render(request, 'seat.html', {'movie': movie, 'seat': seat})
