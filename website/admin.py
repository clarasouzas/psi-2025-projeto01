from django.contrib import admin

from .models import Ator,App,ConteudoPagina, Galeria

admin.site.register(App)
admin.site.register(ConteudoPagina)
class GaleriaInline(admin.TabularInline):
    model = Galeria
    extra = 5

@admin.register(Ator)
class AtorAdmin(admin.ModelAdmin):
    inlines = [GaleriaInline]

admin.site.register(Galeria)
