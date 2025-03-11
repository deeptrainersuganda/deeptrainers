from django.db import models

class About(models.Model):
    mission = models.TextField()
    vision = models.TextField()
    history = models.TextField()

    def __str__(self):
        return "About DTU"


class Contact(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.email
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image = models.ImageField(upload_to='training_images/', default='default.jpg')

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class GalleryCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class GalleryImage(models.Model):
    category = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery/')
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.description or "Gallery Image"