"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    print(data)
    for i in range(0, len(data)):
        subject = data[i]
        print("{} is taught by {} and has {} students".format(subject[0], subject[1], subject[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    count_lines = 0
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        count_lines += 1
    input_file.close()
    input_file = open(FILENAME)
    list_lines = [i for i in range(count_lines)]
    index = 0
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        list_lines[index] = parts
        index += 1
    input_file.close()
    return list_lines


main()
