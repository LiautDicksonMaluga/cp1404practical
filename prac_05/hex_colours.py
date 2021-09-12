COLOUR_CODES = {"DarkGoldenrod": "#b8860b", "DarkOrange": "#ff8c00", "DarkOrchid": "#9932cc", "cyan1": "#00ffff",
                "cornsilk1": "#fff8dc", "cornsilk4": "#8b8878", "chartreuse4": "#458b00", "chocolate": "#cd661d",
"CornflowerBlue": "#6495ed", "burlywood4": "8b7355"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name")
