# This is an auto-generated Django model module.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    customer_name = models.TextField()
    customer_surname = models.TextField() 
    customer_dni = models.TextField(db_column='customer_DNI')  
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente=models.TextField()
    
    # def obtener_cuenta(self):
    #     try:
    #         cuenta = Cuenta.objects.get(customer_id=self.customer_id)
    #         return cuenta
    #     except Cuenta.DoesNotExist:
    #         return None
        
    @receiver(post_save, sender=User)
    def create_cliente(sender, instance, created, **kwargs):
        if created:
            Cliente.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_cliente(sender, instance, **kwargs):
        instance.cliente.save()    
        
    def __str__(self):
        return f"{self.user}'s Profile"
    class Meta:
        managed = False
        db_table = 'cliente'
