from django.contrib import admin

from .models import Manual, UnitManual


class ManualAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'short_name', 'description',
                    'version', 'commencement_date', 'pub_date')
    search_fields = ('version', 'commencement_date')
    list_filter = ('pub_date', 'version')
    empty_value_display = '-не указано-'


admin.site.register(Manual, ManualAdmin)


class UnitManualAdmin(admin.ModelAdmin):
    list_display = ('id', 'manual', 'code_unit', 'value_unit', 'pub_date')
    list_filter = ('pub_date',)
    empty_value_display = '-не указано-'


admin.site.register(UnitManual, UnitManualAdmin)
