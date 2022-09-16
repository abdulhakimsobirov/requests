from django.contrib import admin
from .models import Objects, Brigadir, Requests
from import_export.admin import ImportExportModelAdmin



class ObjectsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name')

class BrigadirAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')

class RAdmin(admin.StackedInline):
    model = Requests
    filter_horizontal = ('dinner', )

class RequestsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RAdmin
    # 
    list_display = ('id', 'date', 'brigadir', 'object', 'lunch', 'dinner', 'late_dinner', )
    



admin.site.register(Objects, ObjectsAdmin)
admin.site.register(Brigadir, BrigadirAdmin)
admin.site.register(Requests, RequestsAdmin)
