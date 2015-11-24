# coding=utf-8
from django.utils.translation import gettext as _
from django.shortcuts import render
from .forms import CartridgeForm
from .models import Cartridge

def index(request):
    title = _('Welcome')
    form = CartridgeForm(request.POST or None)
    order = Cartridge.objects.all()
    if form.is_valid():
        form.save()
    context = {
        'title': title,
        'form': form,
        'order': order,
    }
    return render(request, 'base.html', context)
