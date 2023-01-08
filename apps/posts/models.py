from django.db import models

# Create your models here.

class Authors(models.Model):
    name = models.CharField(max_length=77)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Автора"
        verbose_name_plural = "Авторы"
        
        
class Books(models.Model):
    name = models.CharField(max_length=66)
    post = models.FileField(upload_to='post/')
    authors = models.ManyToManyField(Authors, verbose_name="Авторы")
    pages = models.FileField(upload_to='pages/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Книгу"
        verbose_name_plural = "Книги"
    
class Category(models.Model):
    title = models.CharField(max_length=111)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"
 
    