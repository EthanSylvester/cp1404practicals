def main():
    entry = input("Enter 5 numbers, separated with spaces: ")
    numbers = entry.split(' ')
    for i in range(0, 5):
        numbers[i] = int(numbers[i])
        print("Number: {}".format(numbers[i]))
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[4]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is {}".format(sum(numbers)/len(numbers)))


main()
