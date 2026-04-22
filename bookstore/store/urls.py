from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:id>/', views.book_detail, name='detail'),
    path('search/', views.search, name='search'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('cart/', views.cart, name='cart'),
    path('add-cart/<int:id>/', views.add_to_cart),
    path('wishlist/<int:id>/', views.add_to_wishlist),
    path('checkout/', views.checkout),
    path('review/<int:id>/', views.add_review),
    path('add-book/', views.add_book, name='add_book'),
]