for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
n = int(input("Input number of stars to generate: "))
for i in range(0, n):
    print("*", end='')
print()
n = int(input("Input number of lines of stars to generate: "))
for i in range(1, n + 1):
    for f in range(0, i):
        print("*", end='')
    print()
