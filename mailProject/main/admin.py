from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(AdvUser)
class AdvUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'dolzn']


@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ['sender', 'recipient', 'theme', 'description']


@admin.register(Dolzn)
class DolznAdmin(admin.ModelAdmin):
    list_display = ['name']
