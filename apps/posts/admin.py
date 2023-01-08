from django.contrib import admin
from apps.posts.models import Books, Authors, Category

# Register your models here.
admin.site.register(Books)
admin.site.register(Authors)
admin.site.register(Category)