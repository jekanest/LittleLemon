from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, db_index=True)
    inventory = models.IntegerField(default=6)

    def __str__(self):
      return f'{self.title} : {str(self.price)}'

    
class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=5)
    bookingDate = models.DateField()
 
    def __str__(self): 
        return f'{self.name} : {self.bookingDate} , {self.no_of_guests}'

        

