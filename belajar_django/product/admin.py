from django.contrib import admin

from .models import Category, Product, Status


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "get_category", "get_status")
    search_fields = ("name",)
    list_filter = ("category_id", "status_id")

    def get_category(self, obj):
        return obj.category_id.name

    get_category.short_description = "Kategori"  # type: ignore

    def get_status(self, obj):
        return obj.status_id.name

    get_status.short_description = "Status"  # type: ignore


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


class StatusAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


admin.site.register(Category, CategoryAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Product, ProductAdmin)
