"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)
max_code_length = max(len(code) for code in CODE_TO_NAME.keys())

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:<{max_code_length}} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

for code, name in CODE_TO_NAME.items():
    print(f"{code:<{max_code_length}} is {name}")
