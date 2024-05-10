temperature_readings = [25, 0, 4, 37, 12, 85, 14, 63, 7, 10, -3, 20, 56]
placestoland = []
for temperature in temperature_readings:
    if 0 <= temperature <= 20:
        placestoland.append(temperature)
print("Landing zones:", placestoland)
