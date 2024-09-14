from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Product)
admin.site.register(models.ProductImage)
admin.site.register(models.Category)

