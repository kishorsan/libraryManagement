from django.db import models

# Create your models here.
class Genere(models.Model):
    gname = models.CharField()

    def __str__(self):
        return self.gname

class Book(models.Model):
    bname = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=13)
    price = models.IntegerField()
    description = models.TextField()
    photo = models.ImageField(null=True, blank=True,  upload_to="images/")
    genere = models.ForeignKey("Genere", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    

    def __str__(self):
        return self.bname

class User(models.Model):
    fullName = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.IntegerField()
    username = models.CharField()
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.fullName

class Orders(models.Model):
    uid = models.ForeignKey("User", on_delete=models.CASCADE)
    bid = models.ForeignKey("Book", on_delete=models.CASCADE)
    total = models.IntegerField()