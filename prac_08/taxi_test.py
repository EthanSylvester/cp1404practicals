from prac_08.taxi import Taxi

prius = Taxi("Prius 1", 100)
prius.drive(40)
print("{}, ${} for current fare".format(prius, prius.get_fare()))
prius.start_fare()
prius.drive(100)
print("{}, ${} for current fare".format(prius, prius.get_fare()))
