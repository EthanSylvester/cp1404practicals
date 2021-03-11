"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    result = determine_status(score)
    print(result)


def determine_status(score):
    if score < 0 or score > 100:
        result = "invalid input"
    elif score > 90:
        result = "score is excellent"
    elif score > 50:
        result = "score is passable"
    else:
        result = "score is bad"
    return result


main()
