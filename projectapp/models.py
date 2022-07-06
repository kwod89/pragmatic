from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=20, unique=True, null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='project/', null=True)
    created_at = models.DateField(auto_created=True, null=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'