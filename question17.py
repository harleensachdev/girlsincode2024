
conductivity_values = [
    [8.23e8, 2.13e2, 5.62e7, 7.20e4],
    [3.83e3, 2.22e6, 3.20e5, 1.90e5],
    [6.92e4, 8.83e5, 9.28e2, 8.23e7],
    [3.91e8, 4.03e9, 5.82e7, 6.38e8]
]

special_conductivity = 8.23e7

area_number = 0


for conductivity in conductivity_values:
    area_number += 1
    if special_conductivity in conductivity:
        print("Area", area_number, "has the special element.")
