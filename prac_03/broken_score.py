"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

score = float(input("Enter score: "))
if score < 0 or score > 100:
    print("invalid input")
elif score > 90:
    print("score is excellent")
elif score > 50:
    print("score is passable")
else:
    print("score is bad")
