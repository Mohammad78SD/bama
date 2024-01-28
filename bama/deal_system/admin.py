from django.contrib import admin
from .models import car
# Register your models here.

@admin.register(car)
class CarAdmin(admin.ModelAdmin):
    pass