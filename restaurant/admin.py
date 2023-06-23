from typing import Any, List, Optional, Tuple
from django.contrib import admin, messages
from django.db.models.aggregates import Count
from django.db.models.query import QuerySet
from django.db.models import Q
from django.http.request import HttpRequest

from django.urls import reverse
from django.utils.html import format_html, urlencode

from . import models, forms

@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    form = forms.RestaurantModelForm

    actions = ['toogle_delete']
    list_display = ['id', 'name', 'image_tag', 'description', 'branches_count']
    list_per_page = 10
    
    ordering = ['name']
    search_fields = ['name__istartswith', 'description__istartswith']

    fieldsets = (
        (None, {
           'fields': ('name', 'description', 'is_deleted')
        }),
        ('Uploading logo', {
           'fields': ('image_tag', 'logo')
        }),
    )
    readonly_fields = ['image_tag']

    @admin.display(ordering='branches_count')
    def branches_count(self, restaurant):
        url = (reverse('admin:restaurant_branch_changelist')
               + '?' 
               + urlencode({
                   'restaurant__id': str(restaurant.id)
                }))
        
        return format_html('<a href="{}">{}</a>', url, restaurant.branches_count)
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).annotate(
            branches_count=Count('branch')
        ).filter(~Q(is_deleted=1))
    
    @admin.action(description="Toogle delete")
    def toogle_delete(self, request, queryset):
        updated_count = queryset.update(is_deleted=1)
        self.message_user(
            request,
            f'{updated_count} restaurants where successfully called delete toogle',
            messages.ERROR
        )

# Register your models here.
@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'restaurant_name', 'address']
    list_editable = ['address']
    list_per_page = 10

    list_select_related = ['restaurant']

    def restaurant_name(self, branch):
        return branch.restaurant.name

@admin.register(models.MenuCategory)
class MenuCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'restaurant_name', 'branch_id']
    list_select_related = ['branch', 'branch__restaurant']

    def restaurant_name(self, menu_category):
        return menu_category.branch.restaurant.name

@admin.register(models.MenuPosition)
class MenuPositionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'branch_id', 'description', 'price', 'discount', 'is_available', 'is_deleted']

    def branch_id(self, menu_position):
        return menu_position.menu_category.id

admin.site.register(models.Waiter)
admin.site.register(models.Table)