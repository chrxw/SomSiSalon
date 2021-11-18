from django.contrib import admin

# Register your models here.

from .models import Customer
from .models import Employee
from .models import AboutUs
from .models import Reward
from .models import PaymentMethod
from .models import Product
from .models import Service
from .models import Order
from .models import Appointment
from .models import Receipt
from .models import Promotion
from .models import Notifies

admin.site.register(Customer)
admin.site.register(Employee)
admin.site.register(AboutUs)
admin.site.register(Reward)
admin.site.register(PaymentMethod)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Order)
admin.site.register(Appointment)
admin.site.register(Receipt)
admin.site.register(Promotion)
admin.site.register(Notifies)
