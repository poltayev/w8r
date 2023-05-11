from django.contrib import admin
from . import models

@admin.register(models.Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_deleted', 'restaurant_status']
    list_editable = ['is_deleted']
    list_per_page = 10

    @admin.display(ordering='is_deleted')
    def restaurant_status(self, restaurant):
        if restaurant.is_deleted:
            return 'Deteted'

        return 'OK'

# Register your models here.
@admin.register(models.Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ['id', 'address', 'restaurant_name']
    list_editable = ['address']
    list_per_page = 10

    list_select_related = ['restaurant']

    def restaurant_name(self, branch):
        print(branch)
        return branch.restaurant.name
    
admin.site.register(models.Waiter)
admin.site.register(models.Table)
admin.site.register(models.Menu)
admin.site.register(models.MenuPosition)