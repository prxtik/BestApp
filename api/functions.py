
from math import sin, cos, sqrt, atan2, radians
from datetime import datetime
from .models import BreakDownBus,RequestLog,BusDepot,Supply
class Bus:
    def addData(self,data):
        location={}
        location['bus_no'] = data['bus_no']
        location['route_no'] = data['route_no']
        location['latitude'] = data['latitude']
        location['longitude'] = data['longitude']
        location['timestamp'] = data['timestamp']
        location['status'] = 'O'
        loc = {}
        loc['latitude'] = location['latitude']
        loc['longitude'] = location['longitude']
        location['location'] = str(loc)
        print(str(location))
        bus = BreakDownBus(
            bus_no = location['bus_no'],
            route_no = location['route_no'],
            breakDown_Lat = location['latitude'],
            breakDown_Lon = location['longitude'],
            status = location['status']
        )
        log = RequestLog(
            BusNo = location['bus_no'],
            routeNo = location['route_no'],
            logTime = str(datetime.now()),
            location = location['location'],
            depotAssigned = "None",
            CurrentStatus = location['status']
        )
        bus.save()
        log.save()
        self.assignSupplyBus(location)
        

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

    def nearestDepotList(self, location):
        getData = []
        getData = self.getDepotData()
        for i in getData:
            i['distance'] = self.distance(location['longitude'],location['latitude'], i['latitude'],i['longitude'])
        
        getData.sort(lambda x,y : cmp(x['distance'], y['distance']))
        print(str(getData))
        return getData

        
    

    def getDepotData(self):
        """
            This function returns a list of dictionaries that contains all the depot data for
            calculating the distance from the break down bus and selecting the nearest supply bus.
        """
        depotData = list(BusDepot.objects.all().values())
        return depotData
    
    def createRequestLog(self, bus):
        pass
    
    def assignSupplyBus(self,bus):
        DepotList = self.nearestDepotList(bus)
        for i in DepotList:
            query = Supply.objects.filter(depotno = i['depotNo'],status='AVAIL').values().first()
            if query != None:
                query.status = 'NA'
                print(" bus assigned  info "+ str(query))
                log = RequestLog(
                    BusNo = bus['bus_no'],
                    routeNo = bus['route_no'],
                    logTime = str(datetime.now()),
                    location = bus['location'],
                    depotAssigned = query.depotno,
                    CurrentStatus = 'Assigned'
                )
                log.save()
                query.save(update_fields = ['status'])
                break
            else:
                continue
            
        return query
    
    
    
    def getBrokenBusLocation(self):
        location = BreakDownBus.objects.all().first()
        loc = {}
        loc['latitude'] =location.breakDown_Lat
        loc['longitude']=location.breakDown_Lon
        return loc





