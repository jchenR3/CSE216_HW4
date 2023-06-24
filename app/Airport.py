import math

class Airport:

    def __init__(self, initCode, initLatitudeDegrees, initLatitudeMinutes, initLongitudeDegrees, initLongitudeMinutes):
        self.code = initCode
        self.latitudeDegrees = initLatitudeDegrees
        self.latitudeMinutes = initLatitudeMinutes
        self.longitudeDegrees = initLongitudeDegrees
        self.longitudeMinutes = initLongitudeMinutes
    
    def getCode(self):
        return self.code
    
    def getLatitudeDegrees(self):
        return self.latitudeDegrees
    
    def getLatitudeMinutes(self):
        return self.latitudeMinutes
    
    def getLongitudeDegrees(self):
        return self.longitudeDegrees
    
    def getLongitudeMinutes(self):
        return self.longitudeMinutes
    
    def calculateDistance(a1, a2):
        PI_F = 3.14159265358979
        RADIAN_FACTOR = 180.0 / PI_F
        EARTH_RADIUS = 3963.0

        lat1 = a1.latitudeDegrees + a1.latitudeMinutes / 60.0
        lat1Rad = lat1 / RADIAN_FACTOR
        long1 = -a1.longitudeDegrees + a1.longitudeMinutes / 60.0
        long1Rad = long1 / RADIAN_FACTOR
        lat2 = a2.latitudeDegrees + a2.latitudeMinutes / 60.0
        lat2Rad = lat2 / RADIAN_FACTOR
        long2 = -a2.longitudeDegrees + a2.longitudeMinutes / 60.0
        long2Rad = long2 / RADIAN_FACTOR

        x = math.sin(lat1Rad) * math.sin(lat2Rad) + math.cos(lat1Rad) * math.cos(lat2Rad) * math.cos(long2Rad - long1Rad)
        x2 = math.sqrt(1.0 - (x * x)) / x
        distance = EARTH_RADIUS * math.atan(x2)
        return distance