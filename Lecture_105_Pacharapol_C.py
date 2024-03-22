class Vehicle:
    licenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn on : Air")

class Cars(Vehicle):
    def turnOnSunroof(self):
        print("Turn on : Sunroof")

class PickUp(Vehicle):
    def turnOnOffRoad(self):
        print("Turn on : Off-Road")

class Van(Vehicle):
    def turnOntelevision(self):
        print("Turn on : Television")

class EstateCar(Vehicle):
    def turnOnMassageSeat(self):
        print("Turn on : Massage Seat")

car= Cars()
car.turnOnAirConditioner()

pickup = PickUp()
pickup.turnOnAirConditioner()

van = Van()
van.turnOnAirConditioner()

estatecar = EstateCar()
estatecar.turnOnAirConditioner()

