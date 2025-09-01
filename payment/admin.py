from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User


# register model on the admin section
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

# create an orderitem inline
class OrderItemInline(admin.StackedInline):
	model = OrderItem
	extra = 0

# extend order model
class OrderAdmin(admin.ModelAdmin):
	model = Order
	readonly_fields = ["date_ordered"]
	fields = ["user", "full_name", "email", "shipping_address", "amount_paid", "date_ordered", "shipped", "date_shipped"]
	inlines = [OrderItemInline]

# unregister order model
admin.site.unregister(Order)

# re-register order and orderadmin
admin.site.register(Order, OrderAdmin)