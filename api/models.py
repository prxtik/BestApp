from django.db import models

# Create your models here.
class Supply(models.Model):
    bus_no = models.CharField(max_length = 100, primary_key=True)
    route_no = models.IntegerField()

    def __str__(self):
        return "Bus no. "+str(self.bus_no)+"  route no. = "+str(self.route_no)


class BreakDownBus(models.Model):
    bus_no = models.CharField(max_length = 100, primary_key=True)
    route_no = models.IntegerField()
    breakDown_Lat = models.CharField(max_length = 100)
    breakDown_Lon = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100)
    supply_bus_assign = models.CharField(max_length = 255)
    def __str__(self):
        return "Bus no. "+str(self.bus_no)+"  route no. = "+str(self.route_no)+"  supply bus assigned no. "+ str(self.supply_bus_assign)
     
