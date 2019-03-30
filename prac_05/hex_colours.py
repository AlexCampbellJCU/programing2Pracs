colours = {"blue": "#0000ff", "red": "#ff0000",
           "purple": "#9b30ff", "pink": "#ff83fa",
           "orange": "#ffa500", "green": "#00ff7f",
           "yellow": "#ffd700", "cyan": "#00ffff",
           "brown": "#a52a2a", "black": "#000000"}

colour_name = input("Enter a colour name:")
while colour_name != "":
    print("Code for \"{}\" is {}".format(colour_name, colours.get(colour_name)))
    colour_name = input("Enter a colour name:")