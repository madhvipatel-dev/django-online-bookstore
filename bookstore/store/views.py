from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

# ================= HOME =================
def home(request):
    books = Book.objects.all()
    return render(request, 'store/home.html', {'books': books})


# ================= BOOK DETAIL =================
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = Review.objects.filter(book=book)
    return render(request, 'store/detail.html', {'book': book, 'reviews': reviews})


# ================= SEARCH =================
def search(request):
    query = request.GET.get('q')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'store/home.html', {'books': books})


# ================= REGISTER =================
def register(request):
    if request.method == 'POST':
        User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password']
        )
        return redirect('login')
    return render(request, 'store/register.html')


# ================= LOGIN =================
def user_login(request):
    if request.method == 'POST':
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'store/login.html', {'error': 'Invalid credentials'})
    return render(request, 'store/login.html')


# ================= LOGOUT =================
def user_logout(request):
    logout(request)
    return redirect('home')


# ================= CART =================
def add_to_cart(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    book = get_object_or_404(Book, id=id)
    Cart.objects.create(user=request.user, book=book)
    return redirect('cart')


def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')

    items = Cart.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'items': items})


# ================= CHECKOUT =================
def checkout(request):
    if not request.user.is_authenticated:
        return redirect('login')

    items = Cart.objects.filter(user=request.user)
    order = Order.objects.create(user=request.user)

    for item in items:
        OrderItem.objects.create(
            order=order,
            book=item.book,
            quantity=item.quantity
        )

    items.delete()
    return render(request, 'store/success.html')


# ================= REVIEW =================
def add_review(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        Review.objects.create(
            user=request.user,
            book_id=id,
            rating=request.POST['rating'],
            comment=request.POST['comment']
        )
    return redirect('detail', id=id)


# ================= ADD BOOK =================
def add_book(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            author=request.POST['author'],
            price=request.POST['price'],
            description=request.POST['description'],
            category_id=request.POST['category']
        )
        return redirect('home')

    categories = Category.objects.all()
    return render(request, 'store/add_book.html', {'categories': categories})

# ================= WISHLIST =================
def add_to_wishlist(request, id):
    if not request.user.is_authenticated:
        return redirect('login')

    book = get_object_or_404(Book, id=id)
    Wishlist.objects.create(user=request.user, book=book)
    return redirect('home')