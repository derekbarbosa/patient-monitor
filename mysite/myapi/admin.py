from django.contrib import admin

from .models import User, Device, MedHistory, Allergies, Medications, Operation, Measurement, Measurements

# Register your models here.
admin.site.register(User)
admin.site.register(Device)
admin.site.register(MedHistory)
admin.site.register(Allergies)
admin.site.register(Medications)
admin.site.register(Operation)
admin.site.register(Measurement)
admin.site.register(Measurements)