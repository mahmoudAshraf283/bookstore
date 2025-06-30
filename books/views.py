from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, permission_required
from .models import Book
from .forms import BookForm

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'books/signup.html', {'form': form})

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

@login_required
def book_create(request):
    form = BookForm(request.POST or None)
    if form.is_valid():
        book = form.save(commit=False)
        book.user = request.user
        book.save()
        form.save_m2m()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form})

@login_required
def book_update(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return redirect('book_list')
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('book_list')
    return render(request, 'books/book_form.html', {'form': form})

@login_required
def book_delete(request, pk):
    try:
        book = Book.objects.get(id=pk)
        book.delete()
    except Book.DoesNotExist:
        pass
    return redirect('book_list')

@login_required
def book_detail(request, pk):
    try:
        book = Book.objects.get(id=pk)
    except Book.DoesNotExist:
        return redirect('book_list')
    return render(request, 'books/book_detail.html', {'book': book})
