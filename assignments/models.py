from django.db import models

# Create your models here.
class About(models.Model):
    about_heading=models.CharField(max_length=25)
    about_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='About'     #for spelling correction category to categories djnago auto matically defines it

    def __str__(self):
        return self.about_heading
    
class Sociallinks(models.Model):
    platfrom_name=models.CharField(max_length=25)
    links=models.URLField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.platfrom_name