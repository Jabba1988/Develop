# coding=utf-8
from django.contrib import admin
from .models import Cartridge
from .forms import CartridgeForm


class AdminCartridge(admin.ModelAdmin):
    list_display = ["Manufacturer", "model", "serial_number", "quality_of_filling", "registered_in_service"]
    list_filter = ["quality_of_filling", "model"]
    form = CartridgeForm

admin.site.register(Cartridge, AdminCartridge)

