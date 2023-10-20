from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=30, unique=True)
    hp = models.PositiveIntegerField()
    color = models.CharField(max_length=40)
    description = models.TextField(max_length=1000, blank=True, null=True)
    crated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id} 'Car' {self.brand}"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.PositiveIntegerField(default=0)
    profession = models.CharField(max_length=40)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Furniture(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=50)
    crated_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.color}"


class Food(models.Model):
    name = models.CharField(max_length=35)
    date = models.DateTimeField()
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.date}"


class Football(models.Model):
    football_match = models.CharField(max_length=50)
    score = models.PositiveIntegerField()
    goal_scorer = models.CharField(max_length=35)
    date = models.DateTimeField()
    line_up = models.TextField(max_length=5000)

    def __str__(self):
        return f"{self.football_match} {self.score}"


class Animal(models.Model):
    name = models.CharField(max_length=50, unique=True)
    type = models.CharField(max_length=30)
    number_of_feet = models.PositiveIntegerField()
    food_type = models.TextField(max_length=1000)
    description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.type}, {self.number_of_feet}"


class Programming_languages(models.Model):
    language_type = models.CharField(max_length=30, unique=True)
    intended_for = models.TextField(max_length=1000)
    description = models.TextField(max_length=15000, blank=True, null=True)

    def __str__(self):
        return f"{self.language_type}"


class Phone(models.Model):
    brand = models.CharField(max_length=50, unique=True)
    made_in = models.CharField(max_length=50)
    RAM = models.PositiveIntegerField()
    processor = models.CharField(max_length=35)
    color = models.CharField(max_length=35)
    description = models.TextField(max_length=10000, blank=True, null=True)

    def __str__(self):
        return f"{self.brand} {self.RAM} {self.color}"


class Perfume(models.Model):
    name = models.CharField(max_length=50, unique=True)
    made_in = models.CharField(max_length=50)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} {self.made_in} {self.price}"


class Clothe(models.Model):
    size = models.FloatField()
    for_Boy_or_Girl = models.CharField(max_length=10)
    price = models.PositiveIntegerField()
    made_in = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.size} {self.for_Boy_or_Girl} {self.price}"
