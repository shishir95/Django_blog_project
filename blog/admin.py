from django.contrib import admin
from .models import Data, Users, Categories, SubCategories

# Register your models here.

admin.site.register(Data)
admin.site.register(Users)
admin.site.register(Categories)
admin.site.register(SubCategories)
