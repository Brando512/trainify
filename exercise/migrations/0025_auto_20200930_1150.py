# Generated by Django 3.0.8 on 2020-09-30 18:50

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0024_user_workouts_users_who_liked'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_workouts',
            name='users_who_liked',
        ),
        migrations.AddField(
            model_name='user_workouts',
            name='users_who_liked',
            field=models.ManyToManyField(blank=True, related_name='liked_workouts', to=settings.AUTH_USER_MODEL),
        ),
    ]
