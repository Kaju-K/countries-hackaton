from django.db import models
from django.contrib.auth.models import User
# from countries_app.models import Country

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    country_origin = models.ForeignKey('countries_app.Country', related_name="profile", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
