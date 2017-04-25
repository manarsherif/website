from django.contrib import admin
from .models import Photo ,ImageClass

#admin.site.register(Photo)
#admin.site.register(ImageClass)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(ImageClass,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available', 'created', 'update','features']
    list_filter = ['available', 'created', 'update', 'category']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Photo, ProductAdmin)


