from time import timezone
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Profile(models.Model):
    user  = models.OneToOneField(User, on_delete=models.CASCADE)
    image= models.ImageField(default='batman.png');
    def __str__(self):
        return f'Perfil de {self.user.username}'
    
class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    
    class Meta: #la clase meta es como se va a comportar una clase, definimos comportamiento
        ordering = ['-timestamp']
        
        def __str__(self):
          return f'{self.user.username}: {self.content}'

       
