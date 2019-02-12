
from math import sin, cos, sqrt, atan2, radians
from .models import BreakDownBus
class Bus:
    queue = []
    brokenbusdata = {}
    def addDataInQueue(self,data):
        location={}
        location['latitude'] = data['latitude']
        location['longitude'] = data['longitude']
        location['timestamp'] = data['timestamp']
        print(str(location))
        self.queue.append(location)

    def popDatafromQueue(self):
        loc = self.queue.pop()
        loc2 = self.getBrokenBusLocation()
        loc['distance'] = self.distance(loc['latitude'],loc['longitude'],loc2['latitude'],loc2['longitude'])
        print(str(loc))
        return loc
    
    def distance(self,latitude1,longitude1,latitude2,longitude2):
        # approximate radius of earth in km
        R = 6373.0
        lat1 = radians(float(latitude1))
        lon1 = radians(float(longitude1))
        lat2 = radians(float(latitude2))
        lon2 = radians(float(longitude2))
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R*c
        return distance

    def getBrokenBusLocation(self):
        location = BreakDownBus.objects.all().first()
        loc = {}
        loc['latitude'] =location.breakDown_Lat
        loc['longitude']=location.breakDown_Lon
        return loc







