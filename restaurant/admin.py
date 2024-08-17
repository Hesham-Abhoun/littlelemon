from django.contrib import admin

# Register your models here.
from .models import Menu, Booking, Profile

admin.site.register(Profile)
admin.site.register(Menu)
admin.site.register(Booking)
