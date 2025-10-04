from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Complaint(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    #here using upload_to='' because here user inputting file so it is stored into images file
    image=models.ImageField(upload_to='images/',blank=True,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title#using self we can see teh title name instead of object1,object2,etc