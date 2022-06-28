from django.contrib import admin
from django.db.models import Sum

from .models import *

admin.site.register(Booking)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(CustomPackage)
admin.site.register(Package)
admin.site.register(Payment)
admin.site.register(Testimonial)
@admin.register(BookingSummary)

class BookingSummaryAdmin(admin.ModelAdmin):
    change_list_template = 'admin/booking_summary.html'
    date_hierarchy = 'paymentBooking__datePayment'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'total_sales': Sum('paymentBooking__pricePayment'),
        }

        response.context_data['summary'] = list(
            qs
            .values('codeBooking', 'paymentBooking__datePayment', 'id', 'paymentBooking__methodPayment', 'customerBooking__emailCustomer')
            .annotate(**metrics)
            .order_by('-paymentBooking__datePayment')
        )

        response.context_data['summary_total'] = dict(
            qs.aggregate(**metrics)
        )

        return response
