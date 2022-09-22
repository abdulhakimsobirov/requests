from django.contrib import admin
from .models import Objects, Brigadir, Requests
from import_export.admin import ImportExportModelAdmin



class ObjectsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'brigadir', 'is_active')

class BrigadirAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'is_active')




class RequestsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    
    list_display = ('id', 'date', 'object', 'lunch', 'dinner', 'late_dinner', 'is_active' )
    



admin.site.register(Objects, ObjectsAdmin)
admin.site.register(Brigadir, BrigadirAdmin)
admin.site.register(Requests, RequestsAdmin)
