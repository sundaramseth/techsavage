from django.contrib import admin
from .models import  Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('postname', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['postname', 'job_description']
    prepopulated_fields = {'slug': ('postname',)}

admin.site.register(Job, JobAdmin)
