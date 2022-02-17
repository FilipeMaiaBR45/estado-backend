from django.contrib import admin

from .models import State

# Register your models here.
class StateAdmin(admin.ModelAdmin):
    search_fields = ["modelo"]
    list_display = (
        "id",
        "abreviacao",
        "unidadeFederativa",
        "area",
        "populacao",
        "pib",
    )


admin.site.register(State, StateAdmin)
