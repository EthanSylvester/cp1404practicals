import wikipedia

entry = "Wikipedia"
while entry != "":
    print("Enter the name of a Wikipedia article.")
    entry = input(">>> ")
    if entry == "":
        pass
    else:
        try:
            webpage = wikipedia.page(entry, auto_suggest=False)
            print(webpage.title)
            print(webpage.summary)
            print(webpage.url)
        except wikipedia.exceptions.PageError:
            print(f"{entry} page does not exist. Please try another name.")
        except wikipedia.exceptions.DisambiguationError as error:
            print(", ".join(error.options))
