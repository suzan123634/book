from django.contrib import admin
from product.models import Category, Brand, UnitMeasure, Product, Images
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_by', 'created_at','status', 'image_tag']
    search_fields = ('title',)
    list_filter = ['status']
    readonly_fields = ('image_tag',)
    
class BrandAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']

class UnitMeasureAdmin(admin.ModelAdmin):
    list_display= ['name', 'created_at']

class ProductImageInline(admin.TabularInline):
    model = Images
    extra = 5

class ProductAdmin(admin.ModelAdmin):
    list_display = ['internal_reference','name', 'brand','category', 'sales_price', 'cost_price', 'on_hand', 'unit_measure', 'created_by', 'created_at', 'status', 'image_tag']
    search_fields = ('name',)
    date_hierarchy = 'created_at'
    #list_filter = ['status']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInline]



admin.site.register(Category, CategoryAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(UnitMeasure, UnitMeasureAdmin)
admin.site.register(Images)
admin.site.register(Product, ProductAdmin)

