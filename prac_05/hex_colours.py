"""Hex Colours"""

COLOUR_NAME_TO_HEX_CODE = {"aliceblue": "#f0f8ff",
                           "baby pink": "#f4c2c2",
                           "banana mania": "asdf",
                           "dark byzantium": "#5d3954",
                           "heliotrope": "#df73ff",
                           "pictorial carmine": "#c30b4e",
                           "rebeccapurple": "#663399",
                           "school bus yellow": "#ffd800",
                           "tiffany blue": "#0abab5",
                           "xanadu": "#738678"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        hex_code = COLOUR_NAME_TO_HEX_CODE[colour_name]
        print(f"Hex code: {hex_code}")
    except KeyError:
        print(f"Invalid colour name!")
    colour_name = input("Enter colour name: ").lower()
