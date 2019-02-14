from django.db import models

# Create your models here.
class Supply(models.Model):
    bus_no = models.CharField(max_length = 100, primary_key=True)
    route_no = models.IntegerField()
    depotno = models.IntegerField( default=0)
    supply_bus_no = models.IntegerField(default = 0)
    status = models.CharField(max_length = 100, null =True, blank = True)

    def __str__(self):
        return "Bus no. "+str(self.bus_no)+"  route no. = "+str(self.route_no)+" depot no. = "+ str(self.depotno)


class BreakDownBus(models.Model):
    bus_no = models.CharField(max_length = 100, primary_key=True)
    route_no = models.IntegerField()
    breakDown_Lat = models.CharField(max_length = 100)
    breakDown_Lon = models.CharField(max_length = 100)
    status = models.CharField(max_length = 100)
    supply_bus_assign = models.CharField(max_length = 255, null = True, blank =True)
    def __str__(self):
        return "Bus no. "+str(self.bus_no)+"  route no. = "+str(self.route_no)+"  supply bus assigned no. "+ str(self.supply_bus_assign)
     

class BusDepot(models.Model):
    depotName = models.CharField(max_length = 100)
    depotNo = models.IntegerField(primary_key=True)
    depotLat = models.CharField(max_length=100)
    depotLon = models.CharField(max_length = 100)
    supplyBusValue = models.IntegerField(null = True)
    def __str__(self):
        return "Depot no. "+str(self.depotNo)+" Depot Name: "+str(self.depotName)+" Supply Capacity: "+str(self.supplyBusValue)


class RequestLog(models.Model):
    BusNo = models.CharField(max_length = 100)
    routeNo = models.IntegerField()
    logTime = models.CharField(max_length = 255)
    location = models.TextField(null=True,blank=True)
    depotAssigned = models.CharField(max_length = 255)
    currentStatus = models.CharField(max_length = 255)

    def __str__(self):
        return "Bus no. : "+str(self.BusNo)+",  routeNo : "+str(self.routeNo)+", timeStamp : "+str(self.logTime)
