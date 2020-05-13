from django.contrib import admin
from . models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #fields = (('name', 'slug'), 'description')
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
#admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    #list_display_links = ['name']
    list_display = ['name', 'price', 'stock', 'category', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'category', 'available']
    list_filter = ['name', 'price', 'stock', 'available', 'created', 'updated']
    search_fields = ['name', ]
    #raw_id_fields = ('category',)
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20

admin.site.register(Product, ProductAdmin)

