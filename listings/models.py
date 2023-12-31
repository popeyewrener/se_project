from django.db import models
from datetime import datetime
from Core.models import User
from .modelchoices import category_choices, hostel_choices,semester_choices
# Create your models here.
class Listing(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(default='Books',max_length=100, choices=category_choices,null=True)
    room = models.IntegerField()
    semester = models.CharField(default='BTech 1st',max_length=100,choices=semester_choices,null=True)
    hostel = models.CharField(default='Kurukshetra Hostel',max_length=100,choices=hostel_choices,null=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    total_rating = models.IntegerField(null=True)
    no_of_rating = models.IntegerField(null=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateField(default=datetime.now)

    def __str__(self):
        return self.title
    
    
