HEX_CODE_NAME = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7", "beige": "#f5f5dc", "black": "#000000",
                 "blanchedalmond": "#ffebcd", "blueviolet": "#8a2be2", "brown": "#a52a2a", "burlywood": "#deb887",
                 "cadetblue": "#5f9ea0", "chocolate": "#d2691e"}
colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    if colour_name in HEX_CODE_NAME:
        print(colour_name, "has a code of", HEX_CODE_NAME[colour_name])
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
