from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64)


class Institution(models.Model):
    TYPES = (
        ("fundacja", "fundacja"),
        ("organizacja pozarządowa", "organizacja pozarządowa"),
        ("zbiórka lokalna", "zbiórka lokalna"),
    )
    name = models.CharField(max_length=64)
    description = models.TextField()
    type = models.CharField(choices=TYPES, max_length=64, default="fundacja")
    categories = models.ManyToManyField(Category)

    def lists(self):
        lt = list(self.categories.values_list())
        return ', '.join([item for t in lt for item in t if not isinstance(item, int)])


class Donation(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(Category)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)
    address = models.CharField(max_length=64)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=10)
    pick_up_date = models.DateField()
    pick_up_time = models.DateTimeField(auto_now_add=True)
    pick_up_comment = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
