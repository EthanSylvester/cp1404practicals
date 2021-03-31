user_text = input("Text: ").split()
longest = 1
for i in user_text:
    if len(i) > longest:
        longest = len(i)
longest += 1
word_counts = {k: user_text.count(k) for k in user_text}
for key, value in word_counts.items():
    print("{} : {:>{}}".format(key, value, longest - len(key)))
