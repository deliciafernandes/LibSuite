from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image

class Book(models.Model):
	title = models.CharField(max_length=100)
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	branch = models.CharField(max_length=100)
	subject = models.CharField(max_length=100)