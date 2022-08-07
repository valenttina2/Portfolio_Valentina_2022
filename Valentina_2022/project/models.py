from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100) #поле с символами, ограничено по длине
    description = models.TextField() #поле с текстом, не ограничено
    technology = models.CharField(max_length=50)
    image = models.FileField(upload_to='img/') #поле с файлом изображения, которое хранится в папке img