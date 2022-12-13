from django.contrib import admin
from .models import Categories, Equipment, Calculator


admin.site.register(Categories)


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):

    list_display = ('category', 'make_and_model', 'slug', 'created_on', 'approved')
    prepopulated_fields = {'slug': ('make_and_model',)}
    list_filter = ('approved', 'created_on')
    actions = ['approve_equipment']

    def approve_equipment(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):

    list_display = ('make_and_model', 'slug', 'exposure_duration_hours', 'exposure_duration_minutes')
    prepopulated_fields = {'slug': ('make_and_model','exposure_duration_hours','exposure_duration_minutes')}
