from django.contrib import admin
from products.models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category
    search_fields = ('name',)
    list_display = ('name', 'created_at', 'updated_at')
    list_filter = ()
    filter_horizontal = ()
    ordering = []
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name',)
        }),

    )


class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ('name', "price")
    list_display = ('name', "seller", "price", 'created_at', 'updated_at')
    list_filter = ()
    filter_horizontal = ()
    ordering = []
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name', "category", "seller", 'price', "image", "description")
        }),

    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
