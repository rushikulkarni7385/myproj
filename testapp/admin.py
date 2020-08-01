from django.contrib import admin
from testapp.models import Hyd_Jobs,Pune_Jobs,Banglore_Jobs,Chennai_Jobs

# Register your models here.
class Hyd_JobsAdmin(admin.ModelAdmin):
    list_display = ['Company_Name','Job_Title','Experience','Location','Salary','Posted_date','Qualification']

class Pune_JobsAdmin(admin.ModelAdmin):
    list_display = ['Company_Name','Job_Title','Experience','Location','Salary','Posted_date','Qualification']

class Banglore_JobsAdmin(admin.ModelAdmin):
    list_display = ['Company_Name','Job_Title','Experience','Location','Salary','Posted_date','Qualification']

class Chennai_JobsAdmin(admin.ModelAdmin):
    list_display = ['Company_Name','Job_Title','Experience','Location','Salary','Posted_date','Qualification']

admin.site.register(Hyd_Jobs,Hyd_JobsAdmin)
admin.site.register(Pune_Jobs,Pune_JobsAdmin)
admin.site.register(Banglore_Jobs,Banglore_JobsAdmin)
admin.site.register(Chennai_Jobs,Chennai_JobsAdmin)


