from django.contrib import admin
from django.utils.safestring import mark_safe  # Importa mark_safe
from .models import Exhibition, Exhibition_View

class ExhibitionViewInline(admin.TabularInline):
    model = Exhibition_View
    fields = ('title', 'description', 'display_image')
    extra = 0
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        else:
            return 'No image'

    display_image.short_description = 'Image'

class ExhibitionAdmin(admin.ModelAdmin):
    inlines = [ExhibitionViewInline]
    list_display = ('title',)

admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Exhibition_View)
