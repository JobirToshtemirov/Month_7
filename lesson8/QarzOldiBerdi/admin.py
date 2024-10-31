from django.contrib import admin
from .models import CustomUser, Debt

admin.site.register(CustomUser)
admin.site.register(Debt)
