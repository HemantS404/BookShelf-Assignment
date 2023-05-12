# Generated by Django 4.2.1 on 2023-05-11 06:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cover', models.ImageField(upload_to='BooksCover/')),
                ('genre', models.CharField(choices=[('Fantasy', 'Fantasy'), ('Science Fiction', 'Science Fiction'), ('Adventure', 'Adventure'), ('Detective & Mystery', 'Detective & Mystery'), ('Horror', 'Horror'), ('Romance', 'Romance'), ('Personal Development', 'Personal Development')], max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_book', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
