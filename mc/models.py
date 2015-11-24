# -*- coding: utf-8 -*-
from django.db import models
class Cartridge(models.Model):
    good = "satisfactorily"
    bad = "unsatisfactorily"
    choice_of_quality = (
        (good, 'хорошее'),
        (bad, 'плохое'),
    )
    Manufacturer = models.CharField(max_length=20, help_text='производитель')
    model = models.CharField(max_length=20, help_text='модель')
    serial_number = models.CharField(max_length=20, help_text='Серийный номер')
    printed_pages = models.CharField(max_length=20, help_text='Кол-во отпечатанных страниц')
    quality_of_filling = models.CharField(max_length=20, choices= choice_of_quality, default=good,
                                          help_text='Качество заправки')
    symptom_victim_services = models.CharField(max_length=300, default='none')
    internal_number = models.CharField(max_length=30)
    date_of_filling = models.DateField(auto_now=False, auto_now_add=False, help_text='дата запрвавки')
    install_cartridge_date = models.DateField(auto_now=False, auto_now_add=True)
    uninstall_cartridge_date = models.DateField(auto_now=False, auto_now_add=True)
    install_cartridge_page_count = models.CharField(max_length=20)
    uninstall_cartridge_page_count = models.CharField(max_length=20)
    registered_in_service = models.DateTimeField(auto_now_add=True)

    def __srt__(self):
        return self.serial_number