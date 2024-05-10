from django.contrib import admin
from .models import Contact , Profile, Upload_cv

# Register your models here.
admin.site.register(Contact)
admin.site.register(Profile)
# admin.site.register(Upload_resume)
admin.site.register(Upload_cv)
