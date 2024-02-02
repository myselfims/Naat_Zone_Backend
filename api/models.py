from django.db import models

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255,unique=True)
    password = models.CharField(max_length=20)
    is_verified = models.BooleanField(default=False)
    subscription = models.ForeignKey(Subscription, on_delete=models.SET_NULL , blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {str(self.subscription)}'


class NaatKhwan(models.Model):
    name = models.CharField(max_length=100)
    image = models.TextField()
    about = models.TextField()

class Naat(models.Model):
    title = models.CharField(max_length=100)
    naat_khwan = models.ForeignKey(NaatKhwan,null=True, blank=True,on_delete=models.SET_NULL)
    source = models.TextField()

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    naat = models.ForeignKey(Naat, on_delete=models.CASCADE)


class Benefit(models.Model):
    benefit = models.CharField(max_length=100)
    icon = models.CharField(max_length=255)

