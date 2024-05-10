import math
def calculatetablet(color, volume):
    colortablets = {
        "Clear": 1,
        "Yellow": 2,
        "Yellowish-Green": 3,
        "Brown": 4
    }
    if color in colortablets:
        neededtablets = math.ceil(colortablets[color] * (volume / 100))
        return neededtablets
    else:
        return "Invalid tablet"
data = [
    ("Yellow", 250),
    ("Brown", 4200),
    ("Clear", 2345),
    ("Yellowish-Green", 345)
]
for color, volume in data:
    print("For {0}cm³ of {1} water, add {2} tablets.".format(volume, color, calculatetablet(color,volume)))
