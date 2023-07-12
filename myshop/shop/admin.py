from django.contrib import admin

# Register your models here.

from django.contrib import admin

# Register your models here.
from .models import  Category, Product, ProducPhoto


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id' ,'name','slug')
    prepopulated_fields = {'slug': ('name',)}

    class Meta:
        model = Category

admin.site.register(Category, CategoryAdmin)


class ProducPhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'photo', 'is_active','time_create','time_update')

    class Meta:
        model = ProducPhoto

class ProducPhotoInline(admin.TabularInline):
    model = ProducPhoto
    extra = 0


admin.site.register(ProducPhoto, ProducPhotoAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug','category', 'price','available','created','updated','stock')
    list_filter = ['available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ProducPhotoInline] # Тут звязок з фотографіями

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


