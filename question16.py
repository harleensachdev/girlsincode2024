
pi = 3.14159
radius = float(input("Enter the radius of the Earth (in kilometers): "))
circumferenceofearth = 2* 3.14 * radius * 1000
def calculate_water_percentage(total_surface_area, water_area):
    water_percentage = (water_area / total_surface_area) * 100
    return water_percentage
total_surface_area = float(input("Enter the total surface area of the Earth (in square kilometers): "))
water_area = float(input("Enter the area covered by water (in square kilometers): "))
water_percentage = calculate_water_percentage(total_surface_area, water_area)

print("Circumference of the Earth: {} kilometers".format( round(circumferenceofearth, 2)))
print("Percentage of water coverage: {} %".format(water_percentage))
