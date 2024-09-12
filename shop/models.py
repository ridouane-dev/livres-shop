from django.db import models
#create models here

class Category(models.Model):
    name= models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now=True)

    class Meta:
         ordering =['-date_added']

    def __str__(self) :
         return self.name

class Product(models.Model):
     title = models.CharField(max_length=200)
     price = models.FloatField()
     description = models.CharField(max_length=200)
     categorie = models.ForeignKey(Category, related_name='categorie',on_delete=models.CASCADE)
     image = models.ImageField(upload_to='images/')
     date_added = models.DateTimeField(auto_now=True)
     class Meta:
         ordering =['-date_added']

     def __str__(self) :
         return self.title
     def get_image_url(self):
          if self.image:
               return self.image.url
          return None
     
class Commande(models.Model):
     items = models.CharField(max_length=300)
     total = models.CharField(max_length=200)
     Nom = models.CharField(max_length=150)
     Telephone = models.CharField(max_length=50)
     Address = models.CharField(max_length=200)
     Quartier = models.CharField(max_length=200)
     Regions = models.CharField( default="Niamey", max_length=300)
     zipcode = models.CharField(max_length=300 , default=171) 
     date_commande = models.DateTimeField(auto_now=True)

     class Meta:
          ordering = ['-date_commande']


     def __str__(self) :
         return self.Nom







     
