from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user =  models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return str(self.user)

class Menu(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
         return f'{self.name} : {str(self.price)}'


class Booking(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    booking_date = models.DateTimeField()
    number_of_guests = models.IntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.booking_date}"


@receiver(post_save,sender=User)
def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(
                user= instance
            )