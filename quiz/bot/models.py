from django.db import models


# Create your models here.
class Log(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    messages = models.JSONField(default={'state': 0})


class User(models.Model):
    user_id = models.BigIntegerField(primary_key=True)
    username = models.CharField(max_length=128, null=True)
    first_name = models.CharField(max_length=128, null=True)
    name = models.CharField(max_length=128, null=True)
    phone = models.CharField(max_length=15, null=True)
    A1_1 = models.IntegerField(default=0)
    A1_2 = models.IntegerField(default=0)
    A1_3 = models.IntegerField(default=0)
    A1_4 = models.IntegerField(default=0)
    A1_5 = models.IntegerField(default=0)
    A1_6 = models.IntegerField(default=0)
    A1_7 = models.IntegerField(default=0)
    A2_1 = models.IntegerField(default=0)
    A2_2 = models.IntegerField(default=0)
    A2_3 = models.IntegerField(default=0)
    A2_4 = models.IntegerField(default=0)
    A2_5 = models.IntegerField(default=0)
    A2_6 = models.IntegerField(default=0)
    A2_7 = models.IntegerField(default=0)
    A2_8 = models.IntegerField(default=0)
    B1_1 = models.IntegerField(default=0)
    B1_2 = models.IntegerField(default=0)
    B1_3 = models.IntegerField(default=0)
    B1_4 = models.IntegerField(default=0)
    B1_5 = models.IntegerField(default=0)
    B1_6 = models.IntegerField(default=0)
    B2_1 = models.IntegerField(default=0)
    B2_2 = models.IntegerField(default=0)
    B2_3 = models.IntegerField(default=0)
    B2_4 = models.IntegerField(default=0)
    B2_5 = models.IntegerField(default=0)
    B2_6 = models.IntegerField(default=0)
    B2_7 = models.IntegerField(default=0)
    C1_1 = models.IntegerField(default=0)
    C1_2 = models.IntegerField(default=0)
    C1_3 = models.IntegerField(default=0)
    C1_4 = models.IntegerField(default=0)
    C1_5 = models.IntegerField(default=0)
    C1_6 = models.IntegerField(default=0)
    C1_7 = models.IntegerField(default=0)
    C2_1 = models.IntegerField(default=0)
    C2_2 = models.IntegerField(default=0)
    C2_3 = models.IntegerField(default=0)
    C2_4 = models.IntegerField(default=0)
    C2_5 = models.IntegerField(default=0)
    C2_6 = models.IntegerField(default=0)
    C2_7 = models.IntegerField(default=0)
    total_score = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.username} {self.name}"


# class User_answers(models.Model):

