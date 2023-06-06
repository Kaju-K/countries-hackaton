from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.

class Country(models.Model):
    name = CountryField(max_length=50)

    def __str__(self) -> str:
        return f'{self.name}'
    
class Trip(models.Model):
    country = models.ForeignKey("Country", related_name="trip", on_delete=models.PROTECT)
    user = models.ForeignKey(User, related_name="trip", on_delete=models.CASCADE)
    private_comment = models.CharField(max_length=200, null=True)

    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(
    #             fields=['country', 'user'], name='unique_country_user_combination'
    #         )
    #     ]

    def __str__(self) -> str:
        return f'{self.country}'
    

class Comment(models.Model):
    trip = models.ForeignKey("Trip", on_delete=models.CASCADE, related_name='comment')
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    date = models.DateField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.comment