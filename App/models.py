from django.db import models


class User(models.Model):
    user_name = models.CharField(max_length=16, unique=True)
    user_password = models.CharField(max_length=20)
    user_mail = models.CharField(max_length=30, unique=True)

    class Meta:
        db_table = 'User'
