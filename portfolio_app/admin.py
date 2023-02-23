from django.contrib import admin
#Import model proyects from model
from .models import Exhibition,Exhibition_View


class ExhibitionViewInline(admin.TabularInline):
    model = Exhibition_View

class ExhibitionAdmin(admin.ModelAdmin):
    inlines = [
        ExhibitionViewInline,
    ]

admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Exhibition_View)