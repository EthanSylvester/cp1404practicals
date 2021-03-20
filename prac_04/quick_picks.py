import random

picks = int(input("How many quick picks? "))
for i in range(0, picks):
    numbers = []
    for m in range(0, 6):
        numbers.append(random.randint(1, 45))
    sort_numbers = sorted(numbers)
    print("{:>2} {:>2} {:>2} {:>2} {:>2} {:>2}".format(sort_numbers[0], sort_numbers[1], sort_numbers[2],
                                                       sort_numbers[3], sort_numbers[4], sort_numbers[5]))
