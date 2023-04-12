from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Profile)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Projects)
admin.site.register(models.Skills)
admin.site.register(models.Interests)