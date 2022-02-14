from django.contrib import admin
from django.apps import apps
from .models import GrupoCliente

models = apps.get_models()

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# Register your models here.
