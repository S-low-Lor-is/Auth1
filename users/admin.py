from django.contrib import admin
from .models import Machine, Sell,SellRange
# Register your models here.
admin.site.register(Machine)
admin.site.register(Sell)
admin.site.register(SellRange)

