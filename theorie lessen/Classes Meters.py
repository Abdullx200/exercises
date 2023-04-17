class Distance:
    def __init__(self, value_meters):
        self.value_meters = value_meters

    @staticmethod
    def meteres(value_meteres):
        return value_meteres
    
    @staticmethod
    def millimeters(value_meters):
        return value_meters*1000
    
    @staticmethod
    def miles(value_meters):
        return value_meters/1600
#door dat de methodes static zijn kunnen ze zo gewoon 
Distance.millimeters(30)
print(Distance.millimeters(30))

#d = Distance(30) Dit kan, hier wordt er een object gemaakt en dan wordt het zo geprint
#print(d.millimeters())