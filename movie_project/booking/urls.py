from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('welcome/', views.welcome_view, name='welcome'),
    path('movies/', views.movie_list, name='movie_list'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('book/<int:movie_id>/<int:seat_id>/', views.book_seat, name='book_seat'),
]
