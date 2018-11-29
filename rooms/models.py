from django.db import models
from datetime import datetime
from companies.models import Company


class Room(models.Model):
    HORROW_ACTOR = "HA"
    HORROW = "HW"
    PUZZLE_ACTOR = "PA"
    PUZZLE = "PW"
    COMEDY_ACTOR = "CA"
    COMEDY = "CW"
    POLICE_ACTOR = "PSA"
    POLICE = "PSW"
    KIDS = "KW"
    CATEGORY_CHOICES = (
        (HORROW_ACTOR, "Horrow with actor"),
        (HORROW, "Horrow without actor"),
        (PUZZLE_ACTOR, "Puzzle with actor"),
        (PUZZLE, "Puzzle without actor"),
        (COMEDY_ACTOR, "Comedy with actor"),
        (COMEDY, "Comedy without actor"),
        (POLICE_ACTOR, "Police-Spy with actor"),
        (POLICE, "Police-Spy without actor"),
        (KIDS, "Kids Friendly"),
    )
    DURATION_CHOICES = (
        ("60M", "60 Minutes"),
        ("70M", "70 Minutes"),
        ("80M", "80 Minutes"),
        ("90M", "90 Minutes"),
        ("90+M", "90+ Minutes"),
    )
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)    
    title = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=50)
    category = models.CharField(
        max_length=3, choices=CATEGORY_CHOICES, default="CW")
    duration = models.CharField(
        max_length=3, choices=DURATION_CHOICES, default="60M")
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)    

    def __str__(self):
        return self.title
