from django.contrib import admin
from .models import myUser
from .models import Sport
from .models import Day
from .models import slTime
from .models import Booking

# Register your models here.
admin.site.register(myUser)
admin.site.register(Sport)
admin.site.register(Day)
admin.site.register(slTime)
admin.site.register(Booking)
