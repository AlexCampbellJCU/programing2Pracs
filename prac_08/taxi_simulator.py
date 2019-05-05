from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")
    print("q)uit, c)hoose taxi, d)rive")
    main_menu = input(">>> ").lower()
    while main_menu != "q":
        if main_menu == "c":
            print("Taxis available: ")

            for i, taxi in enumerate(taxis):
                print("{} - {}".format(i, str(taxi)))

            taxi_choice = int(input("Choose taxi: "))
            chosen_taxi = taxis[taxi_choice]

        elif main_menu == "d":
            chosen_taxi.start_fare()
            distance_to_drive = float(input("Drive how far? "))
            chosen_taxi.drive(distance_to_drive)
            trip_cost = chosen_taxi.get_fare()
            print("Your {} trip cost you ${:.2f}".format(chosen_taxi.name, trip_cost))
            total_bill += trip_cost

        else:
            print("Invalid option")
        print("Bill to date: ${:.2f}".format(total_bill))
        print("q)uit, c)hoose taxi, d)rive")
        main_menu = input(">>> ").lower()

    print("Total trip cost: ${:.2f}".format(total_bill))
    print("Taxis are now:")

    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, str(taxi)))

main()