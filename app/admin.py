from django.contrib import admin
from .models import Profile, ParentCategory, MainCategory, SubCategory, DrinkCategory

admin.site.register(Profile)
admin.site.register(ParentCategory)
admin.site.register(MainCategory)
admin.site.register(SubCategory)
admin.site.register(DrinkCategory)
