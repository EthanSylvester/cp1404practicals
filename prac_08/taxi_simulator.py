from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    bill = 0
    selection = None
    print("Let's drive!")
    while selection != "q".lower():
        print("c)hoose taxi, d)rive, q)uit")
        selection = input(">>> ")
        if selection == "c".lower():
            print("Taxis available:")
            print_taxis(taxis)
            choice = int(input("Choose taxi: "))
            try:
                current_taxi = taxis[choice - 1]
            except IndexError or TypeError:
                print("Invalid taxi choice")
        elif selection == "d".lower():
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                if distance < 0:
                    print("Distance must be greater than 0")
                else:
                    current_taxi.drive(distance)
                    fare = current_taxi.get_fare()
                    current_taxi.start_fare()
                    print("Your {} trip cost you ${:.2f}".format(current_taxi.name, fare))
                    bill += fare
            print("Bill to date: ${:.2f}".format(bill))
        elif selection == "q".lower():
            print("Total trip cost: ${:.2f}".format(bill))
            print("Taxis are now:")
            print_taxis(taxis)
        else:
            print("Invalid Option")
            print("Bill to date: ${:.2f}".format(bill))


def print_taxis(taxis):
    for n, taxi in enumerate(taxis):
        print("{} - {}".format(n + 1, taxi))


main()
