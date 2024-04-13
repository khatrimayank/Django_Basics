from django.contrib import admin

from .models import GeeksModel,PostModel

# Register your models here.

admin.site.register(GeeksModel)
admin.site.register(PostModel)