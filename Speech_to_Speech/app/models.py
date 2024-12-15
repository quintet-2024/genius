from django.db import models

# Create your models here.


class login_table(models.Model):
    username=models.CharField(max_length=40)
    password=models.CharField(max_length=40)
    type=models.CharField(max_length=10)

class user_table(models.Model):
    LOGIN=models.ForeignKey(login_table,on_delete=models.CASCADE)
    image=models.FileField()
    email = models.CharField(max_length=40)
    language = models.FileField(max_length=40)

class complaint_table(models.Model):
    USER = models.ForeignKey(login_table,on_delete=models.CASCADE)
    comlaint = models.CharField(max_length=150)
    date = models.DateField
    reply = models.CharField(max_length=150)

class feedback_table(models.Model):
    USER = models.ForeignKey(login_table,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=150)
    rating = models.FloatField
    date = models.DateField

class history_table(models.Model):
    USER = models.ForeignKey
    source_message = models.CharField(max_length=500)
    target_message = models.CharField(max_length=500)
    target_language = models.CharField(max_length=500)
    type = models.CharField(max_length=20)