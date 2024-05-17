from django.db import models
from . helpers import SaveMediaFile


class Country(models.Model):
    name = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Address(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Agency(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    last_update = models.DateTimeField(auto_now=True)


class Agent(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.phone_number}"


class Users(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    image = models.ImageField(upload_to=SaveMediaFile.user_image)
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=10, blank=True)
    ins_link = models.URLField(blank=True)
    face_link = models.URLField(blank=True)
    linked_in = models.URLField(blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.email} {self.username}"


class Testimonials(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFile.testimonial)
    client_name = models.CharField(max_length=100)
    profession = models.CharField(max_length=100)
    star_rating = models.PositiveIntegerField(default=5)

    def __str__(self):
        return self.client_name


class Comments(models.Model):
    comment = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    users = models.ManyToManyField(Users)

    def __str__(self):
        return f"{self.comment} {self.create_date}"