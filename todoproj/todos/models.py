from django.db import models
#We will be using Object Relational MApping in python ORMs
# Create your models here.
# table todo column content
class Todo(models.Model):
    content =models.TextField()

