from django.contrib import admin

from .models import *

admin.site.register(Booking)
admin.site.register(CustomPackage)
admin.site.register(Package)
admin.site.register(Customer)
admin.site.register(Testimonial)