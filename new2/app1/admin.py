from django.contrib import admin

from .models import students, feedback
# from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(students)
admin.site.register(feedback)
# admin.site.register(CustomUser, UserAdmin)