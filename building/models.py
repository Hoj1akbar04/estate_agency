from django.db import models
from users.models import Address
from users.helpers import SaveMediaFile, Choices


class House(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    image = models.ImageField(upload_to=SaveMediaFile.home_image)
    price = models.FloatField()
    area = models.FloatField()
    beds = models.IntegerField()
    baths = models.IntegerField()
    garages = models.IntegerField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.price} {self.area} {self.beds} {self.baths} {self.garages} {self.address}"