from django.contrib import admin
from myapp.models import Book, Genere, User, Orders

# Register your models here.

class BookDetails(admin.ModelAdmin):
    list_display = ['bname', 'ISBN', 'price', 'description', 'genere']

class UserDetails(admin.ModelAdmin):
    list_display = ['fullName', 'email', 'phone', 'username', 'password']

class OrdersDetails(admin.ModelAdmin):
    list_display = ['uid', 'bid', 'total']

admin.site.register(Book, BookDetails)
admin.site.register(Genere)
admin.site.register(User, UserDetails)
admin.site.register(Orders, OrdersDetails)