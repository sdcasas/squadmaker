from django.contrib import admin

from apps.joker.models import Joker


@admin.register(Joker)
class JokerAdmin(admin.ModelAdmin):
    pass