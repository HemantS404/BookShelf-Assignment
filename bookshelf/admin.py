from django.contrib import admin
from .models import Book

class book(admin.ModelAdmin):
    list_display = ('name', 'user', 'genre')

# Register your models here.
admin.site.register(Book, book)