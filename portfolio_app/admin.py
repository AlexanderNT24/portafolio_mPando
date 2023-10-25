from django.contrib import admin
from django.utils.safestring import mark_safe  # Importa mark_safe
from .models import Exhibition, Exhibition_View,BiographyType,Biography

class ExhibitionViewInline(admin.TabularInline):
    model = Exhibition_View
    fields = ('order', 'title', 'description', 'image','display_image')
    extra = 0
    readonly_fields = ('display_image',)
    def display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100" height="100" />')
        else:
            return 'No image'

    display_image.short_description = 'Image'


class BiographyInline(admin.TabularInline):
    model = Biography
    fields = ('date', 'description', 'biography_type')  # Use 'biography_type' field to display BiographyType
    extra = 0

    readonly_fields = ('biography_type',)  # Make 'biography_type' readonly

    def get_type_name(self, obj):
        return obj.biography_type.name

    get_type_name.short_description = 'Biography Type'

 
class ExhibitionAdmin(admin.ModelAdmin):
    inlines = [ExhibitionViewInline]
    list_display = ('title',)

class BiographyAdmin(admin.ModelAdmin):
    inlines = [BiographyInline]
    list_display = ('description',)

class BiographyTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Registra los modelos en el admin
admin.site.register(Exhibition, ExhibitionAdmin)
admin.site.register(Exhibition_View)
admin.site.register(Biography, BiographyAdmin)
admin.site.register(BiographyType, BiographyTypeAdmin)