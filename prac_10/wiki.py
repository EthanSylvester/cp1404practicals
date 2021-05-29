import wikipedia

page = "Wikipedia"
while page != "":
    print("Enter the name of a Wikipedia article.")
    page = input(">>> ")
    try:
        print(wikipedia.summary(page, auto_suggest=False))
    except wikipedia.exceptions.DisambiguationError as error:
        print(error.options)
    except wikipedia.exceptions.PageError:
        print(f"{page} page does not exist. Please try another name.")
