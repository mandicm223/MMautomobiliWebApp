
from django.contrib import admin
from .models import Car
from django.utils.html import format_html
# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self , object):
        return format_html('<img src="{}" width=40 style="border-radius: 50%;" />'.format(object.car_photo.url))

    thumbnail.short_description = 'Car Photo'

    
    list_display = ('id' , 'thumbnail' , 'car_title' , 'city' , 'color' , 'fuel_type' , 'year' , 'body_style' , 'is_featured')
    list_display_links = ('id' , 'thumbnail' , 'car_title',)
    list_editable = ('is_featured',)
    search_fields = ('car_title' , 'city' , 'fuel_type' , 'color' , 'year' , 'body_style')
    list_filter = ('city', 'color' , 'fuel_type' , 'body_style')

admin.site.register(Car , CarAdmin)