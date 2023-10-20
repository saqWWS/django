from django.contrib import admin

from .models import Atalanta, Cagliari, Bologna, Empoli, Fiorentina, Frosinone, Genoa, HellasVerona, Inter, Juventus


@admin.register(Atalanta)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(Cagliari)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(Bologna)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(Empoli)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(Fiorentina)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(Frosinone)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(Genoa)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(HellasVerona)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(Inter)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)


@admin.register(Juventus)
class AdminFootball(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age", "position", "number", "foot", "citizenship")
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "number", "foot", "citizenship", "position",)
    list_filter = ("foot", "position",)
