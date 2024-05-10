
data = [
    ["enzyme A", 21],
    ["enzyme B", 402],
    ["enzyme C", 539],
    ["enzyme D", 384],
    ["enzyme E", 42],
    ["enzyme F", 45],
    ["enzyme G", 450],
    ["enzyme H", 48],
    ["enzyme I", 505],
    ["enzyme J", 60],
    ["enzyme K", 65],
    ["enzyme L", 626],
    ["enzyme M", 73],
    ["enzyme N", 78],
    ["enzyme O", 339]
]
for enzyme, temperature in data:
    temperatureincelsius = round(temperature - 273.15, 1)
    print("enzyme {}: {} °C".format(enzyme, temperatureincelsius))
