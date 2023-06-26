import sys

from pyTPS_Transaction import pyTPS_Transaction

class AddFlight(pyTPS_Transaction):
    
    def __init__(self, initAirport, initStops):
        self.airport = initAirport
        self.stops = initStops

    def doTransaction(self):
        self.stops.append(self.airport)

    def undoTransaction(self):
        self.stops.pop()

    def toString(self):
        return "Add " + self.airport