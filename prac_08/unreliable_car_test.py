from prac_08.unreliable_car import UnreliableCar


def main():
    working_car = UnreliableCar("Top Fueler", 100, 80)
    broken_car = UnreliableCar("Cheap", 100, 10)

    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(working_car.name, working_car.drive(i)))
        print("{:12} drove {:2}km".format(broken_car.name, broken_car.drive(i)))
    print(working_car)
    print(broken_car)


main()