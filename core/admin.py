from django.contrib import admin
from .models import Cpf
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CpfResource(resources.ModelResource):
    class Meta:
        model = Cpf

class CpfAdmin(ImportExportModelAdmin):  
    resource_class = CpfResource

admin.site.register(Cpf, CpfAdmin)
