from django.db import models
from django.shortcuts import reverse
# Create your models here.


class Car(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    no_of_pages = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    @classmethod
    def get_all_cars(cls):
        return cls.objects.all()


    def get_show_url(self):
        return reverse("cars.show",args=[self.id])


    def get_edit_url(self):
        return reverse("cars.edit",args=[self.id])


    def get_delete_url(self):
        return reverse("cars.delete",args=[self.id])