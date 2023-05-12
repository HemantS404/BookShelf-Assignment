from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    genre_choices =  (('Fantasy','Fantasy'),
                      ('Science Fiction','Science Fiction'),
                      ('Adventure','Adventure'),
                      ('Detective & Mystery','Detective & Mystery'),
                      ('Horror','Horror'),
                      ('Romance','Romance'),
                      ('Personal Development','Personal Development'))

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user_book')
    name = models.CharField(max_length = 120)
    cover = models.ImageField(upload_to = 'BooksCover/')
    genre = models.CharField(choices = genre_choices, max_length = 50)
    description = models.CharField(max_length = 500)

    def __str__(self):
        return self.user.username+"'s "+self.name