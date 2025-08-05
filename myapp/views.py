from django.shortcuts import render, redirect
from myapp.models import Book, User
from myapp.forms import bookForm, UserForm

# Create your views here.

def index(request):
    return render(request, 'myapp/index.html')

def login(request):
    loginn = User.objects.all()
    users = {}
    for i in loginn:
        users[i.username] = (i.username, i.password)
    if request.method == "POST": 
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        if username in users:
            if users[username] == (username, password):
                return redirect('/')
    return render(request, 'myapp/login.html')

def signup(request):
    signupp = UserForm()
    if request.method == "POST":
        signupp = UserForm(request.POST)
        if signupp.is_valid():
            signupp.save(commit=True)
            return redirect('/')
    d = {'user': signupp}
    return render(request, 'myapp/signup.html', d)

def password(request):
    return render(request, 'myapp/password.html')

def logout(request):
    return redirect('/')

def home(request):
    b = Book.objects.all()
    data = {'books': b}
    return render(request, 'myapp/home.html', data)

def insertData(request):
    b = bookForm()
    if request.method == 'POST':
        b = bookForm(request.POST)
        if b.is_valid():
            b.save(commit=True)
            return redirect('/')
    d = {'form': b}
    return render(request, 'myapp/insert.html', d)

def updateData(request, id):
    b = Book.objects.get(id=id)
    book = bookForm(instance=b)
    if request.method == 'POST':
        book = bookForm(request.POST, request.FILES, instance=b)
        if book.is_valid():
            book.save(commit=True)
            return redirect(f'/detail/{id}')
    d = {'form': book}
    return render(request, 'myapp/update.html', d)

def deleteData(request, id):
    b = Book.objects.get(id=id)
    b.delete()
    return redirect('/')

def detail(request, id):
    b = Book.objects.get(id=id)
    d = {'book': b}
    return render(request, 'myapp/detail.html', d)

