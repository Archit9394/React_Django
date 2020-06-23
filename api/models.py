from django.db import models

# Create your models here.
class UserAPI(models.Model):
    verbose_name="User1"
    name=models.CharField(max_length=50,unique=False)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)

    class Meta:
        verbose_name="Userapi"
        
    def __str__(self):
        return self.email
