from django.db import models


# Create your models here.
class User(models.Model):
    user_email = models.EmailField(max_length=100, unique=True)
    user_password = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email
