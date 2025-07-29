import os
import sys
import django
from faker import Faker
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryManagement.settings')
django.setup()
f = Faker()

from myapp.models import Book, Genere, User, Orders

generes = Genere.objects.all()
books = Book.objects.all()
users = User.objects.all()

def generate_book_data(n):
    for i in range(n):
        fbname = f.sentence(nb_words=5)
        fISBN = f.isbn13(separator="")
        fprice = random.randint(100, 999)
        fdescription = f.paragraph(nb_sentences=8)
        fphoto = "static/cover.jpg"
        fgenere = random.choice(generes)
        b = Book.objects.get_or_create(bname=fbname, ISBN=fISBN, price=fprice, description=fdescription, photo=fphoto, genere=fgenere)


def generate_user_data(n):
    for i in range(n):
        ffname = f.first_name() + " " + f.last_name()
        femail = f.email()
        number = str(random.randint(6,9)) + "".join(random.choices("0123456789", k=9))
        fphone =  int(number)
        fusername = ffname[:4] + str(random.randint(10,99))
        fpassword = ffname[:4] + ffname[-3:] + "@12."
        u = User.objects.get_or_create(fullName=ffname,  email=femail, phone=fphone, username=fusername, password=fpassword)


def generate_orders_data(n):
    for i in range(n):
        fuid = random.choice(users)
        fbid = random.choice(books)
        ftotal = fbid.price
        o = Orders.objects.get_or_create(uid=fuid, bid=fbid, total=ftotal)


if __name__  == '__main__':
    inputs = sys.argv
    if len(inputs) == 3:
        try:
            choice = int(inputs[1])
            n = int(inputs[2])
            if choice == 1:
                # print(f"You put {choice} & {n}")
                generate_book_data(n)
            elif choice == 2:
                # print(f"You put {choice} & {n}")
                generate_user_data(n)
            elif choice == 3:
                # print(f"You put {choice} & {n}")
                generate_orders_data(n)
            else:
                print(f"You put {choice} & {n}")
                print("Enter a valid input as argument")
        except:
            print("Enter only integers in the below format")
            print("your inputs are ", inputs)
            print("Ex:- py populate.py 1 3")
            print("in the terminal window")
    else:
        print("your input is ", inputs)
        print("Enter in this format")
        print("Ex:- py populate.py 1 3")
        print("in the terminal window")