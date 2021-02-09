from django.db import models
from django.contrib.auth.models import User


def decode_pass(exist_pass):
    return exist_pass[::-1]

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=1000)

class passwords(models.Model):
    hashed_password = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # encoding is as simple as possible, just storing the password reversed
    def encode_pass(new_pass):
        return new_pass[::-1]

    def __str__(self):
        return decode_pass(self.hashed_password)
