# This is an auto-generated Django model module.

from django.db import models
from django.contrib.auth.models import User


class Cliente(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    customer_name = models.TextField()
    customer_surname = models.TextField() 
    customer_dni = models.TextField(db_column='customer_DNI')  
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()

    def __str__(self):
        return f"{self.related_user.username}'s Profile"
    class Meta:
        managed = False
        db_table = 'cliente'
