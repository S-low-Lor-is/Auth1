from django.contrib import admin
from .models import Article, Devices, Sells
# Register your models here.
admin.site.register(Article)
admin.site.register(Devices)
admin.site.register(Sells)

