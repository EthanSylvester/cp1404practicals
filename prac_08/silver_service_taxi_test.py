from prac_08.silver_service_taxi import SilverServiceTaxi

prius = SilverServiceTaxi("Prius 1", 100, 2)
prius.drive(18)
print("{}, ${:.2f} for current fare".format(prius, prius.get_fare()))
prius.drive(100)
print("{}, ${:.2f} for current fare".format(prius, prius.get_fare()))
