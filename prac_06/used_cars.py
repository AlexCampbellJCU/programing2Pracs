"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("My Car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))
    print(my_car)
    print("--------------------------------")

    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(limo.name)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)
    print(limo)
    print("--------------------------------")

    # testing / playing around with the classes

    custom_car = input("Car name")
    custom_fuel = int(input("Fuel amount"))
    custom = Car(custom_car, custom_fuel)
    custom.drive(115)
    print(custom)
    print(custom.fuel, custom.odometer, custom.name)
main()