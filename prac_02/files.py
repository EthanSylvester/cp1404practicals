# Task 1
name = input("Enter user's name: ")
out_file = open('names.txt', 'w')
print(name, file=out_file)
out_file.close()

# Task 2
in_file = open('names.txt', 'r')
username = in_file.read()
in_file.close()
print("Your name is", username)

# Task 3
in2_file = open('numbers.txt', 'r')
num1 = int(in2_file.readline())
num2 = int(in2_file.readline())
in2_file.close()
print(num1 + num2)

# Task 4
in3_file = open('numbers.txt', 'r')
total = 0
for lines in in3_file:
    number = int(lines)
    total = total + number
print(total)
