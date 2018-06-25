from django.contrib import admin

# Register your models here.

from . import models
admin.site.register(models.UserProfile)
admin.site.register(models.Role)
admin.site.register(models.CustomerInfo)
admin.site.register(models.Student)
admin.site.register(models.CustomerFollowUp)
admin.site.register(models.Course)
admin.site.register(models.ClassList)
admin.site.register(models.CourseRecord)
admin.site.register(models.StudyRecord)
admin.site.register(models.Branch)
admin.site.register(models.Menus)


