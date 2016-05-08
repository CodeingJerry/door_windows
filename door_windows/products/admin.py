# coding:utf-8
from django.contrib import admin
from models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('avatar','title','content','status','create_timestamp','last_update_timestamp')
    search_fields = ['title','content']
    actions = ['make_picked']

    def make_picked(self,request,queryset):
        for a in queryset:
            a.status = 10
            a.save()
    make_picked.short_description = u'设置精华'

admin.site.register(Products,ProductsAdmin)