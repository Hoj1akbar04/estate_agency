from django.db import models
from users.models import Country, Comments
from users.helpers import SaveMediaFile


class Travel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to=SaveMediaFile.travel_image)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    comments = models.ManyToManyField(Comments, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.comments}"
