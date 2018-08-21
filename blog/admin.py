from django.contrib import admin
from .models import Post
from import_export.admin import ImportExportModelAdmin
from .models import Ymon
from .models import Person

admin.site.register(Post)


@admin.register(Ymon)
class YmonAdmin(ImportExportModelAdmin):
    pass
    
    
@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    pass