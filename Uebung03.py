import math

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
#---------------------------------------------

class Figur:
    def __init__(self):
        self.name = "Figur"
    
    def umfang(self):
        return 0
        
    def __str__(self):
        return self.name 
    

#---------------------------------------------
class Dreieck(Figur):
    def __init__(self, punkt1, punkt2, punkt3):
        super().__init__('Dreieck')
        self.A = punkt1
        self.B = punkt2
        self.C = punkt3

    def umfang(self):
        seite1 = ((self.punkt1.x - self.punkt2.x) ** 2 + (self.punkt1.y - self.punkt2.y) ** 2) ** 0.5
        seite2 = ((self.punkt2.x - self.punkt3.x) ** 2 + (self.punkt2.y - self.punkt3.y) ** 2) ** 0.5
        seite3 = ((self.punkt3.x - self.punkt1.x) ** 2 + (self.punkt3.y - self.punkt1.y) ** 2) ** 0.5
        return seite1 + seite2 + seite3
    
    def __str__(self):
        return f"{self.name} {self.punkt1}, {self.punkt2}, {self.punkt3}"
#---------------------------------------------
class Rechteck(Figur):
    def __init__(self, punkt1, punkt2):
        super().__init__('Rechteck')
        self.A = punkt1 
        self.B = punkt2

    def umfang(self):
        Seite1 = self.punkt1.y-self.punkt2.y
        Seite2 = self.punkt1.y-self.punkt2.x
        if Seite1 < 0:
            Seite1 * -1
        if Seite2 < 0:
            Seite2 * -1
        return 2*Seite1 + 2*Seite2
    
    def __str__(self):
        return f'{self.name}, {self.punkt1}, {self.punkt2}'
#---------------------------------------------
class Kreis(Figur):
    def __init__(self, mittelpunkt, radius):
        super().__init__('Kreis')
        self.M = mittelpunkt
        self.r = radius

    def umfang(self):
        return math.pi * 2 *self.r
    
    def __str__(self):
        return f'{self.name}, {self.mittelpunkt}, {self.radius}'
#---------------------------------------------
class Polygon(Figur):
    def __init__(self, punkt: list[Punkt]):
        super().__init__("Polygon")
        self.punkt = Punkt

    def distanz(p1, p2):
        return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

    def umfang(self):
        def distanz(p1, p2):
            return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
    
        if len(self.punkt) >= 3:
            umfang = 0
            last = self.punkt[len(self.punkt)-1]  
            for punkt in self.punkt:
                umfang += distanz(punkt, last)
                last = punkt
            return umfang
        else:
            print("Es braucht mindestens 3 Punkte")
           
        return abs(abs(self.C.x-self.A.x)*2 + abs(self.C.y-self.A.y)*2)
 
    def __str__(self):
        PunktStr = ""
        for i in range (len(self.punkt)):
            PunktStr+=f"P{i+1}:{self.punkt[i]} "
                     
        return f"{self.name} {PunktStr}"













k = Kreis(Punkt(0,0), 2)

print(k.name, k.fläche())