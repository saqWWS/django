from django.contrib import admin

from .models import Car, Person, Furniture, Food, Football, Animal, Programming_languages, Phone, Perfume, Clothe


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("id", "brand", "hp", "crated_at", "updated_at")
    list_display_links = ("id", "brand")
    search_fields = ("brand",)
    list_filter = ("color",)


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("id", "brand", "color")
    list_display_links = ("id", "brand")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "age")
    list_display_links = ("id", "first_name", "last_name")


@admin.register(Furniture)
class FurnitureAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "color")
    list_display_links = ("id", "name")


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "date")
    list_display_links = ("id", "name", "date")


@admin.register(Football)
class FootballAdmin(admin.ModelAdmin):
    list_display = ("id", "football_match", "score", "goal_scorer")
    list_display_links = ("id", "football_match", "score")


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type", "number_of_feet")
    list_display_links = ("id", "name")


@admin.register(Programming_languages)
class ProgrammingLanguagesAdmin(admin.ModelAdmin):
    list_display = ("id", "language_type")


@admin.register(Perfume)
class PerfumeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
    list_display_links = ("id", "name", "price")


@admin.register(Clothe)
class ClotheAdmin(admin.ModelAdmin):
    list_display = ("id", "size", "price")
    list_display_links = ("id", "size", "price")
