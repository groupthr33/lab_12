from django.db import models


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class Gift(models.Model):
    name = models.CharField(max_length=20)
    receiver = models.ForeignKey(User, on_delete=models.CASADE, blank=False, null=True, default=None)

