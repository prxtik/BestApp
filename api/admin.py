from django.contrib import admin
from .models import Supply,BreakDownBus,BusDepot,RequestLog
# Register your models here.
admin.site.register(Supply)
admin.site.register(BreakDownBus)
admin.site.register(BusDepot)
admin.site.register(RequestLog)
