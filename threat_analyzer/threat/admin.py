from django.contrib import admin
from .models import Devices, DevicesVariations, SPWithDescription, SPDevices, SPProtection, ThreatWithDescription, SPUBI

admin.site.register(Devices)
admin.site.register(DevicesVariations)
admin.site.register(SPDevices)
# admin.site.register(SPWithDescription)
# admin.site.register(SPProtection)
# admin.site.register(ThreatWithDescription)
# admin.site.register(SPUBI)



# @admin.register(Devices)
# class DevicesAdmin(admin.ModelAdmin):
