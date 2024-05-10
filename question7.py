lowresources = []

def resourceusage(initialresources, rateofusage, days):
    remainingresources = initialresources.copy()
    for day in range(1, days + 1):
        for resource in initialresources:
            remainingresources[resource] -= rateofusage[resource]
            if remainingresources[resource] <= 0:
                if resource not in lowresources:
                    lowresources.append(resource)

    return remainingresources, lowresources

water = float(input("Enter the initial quantity of water (in liters): "))
oxygen = float(input("Enter the initial quantity of oxygen: "))
food = float(input("Enter the initial quantity of food (in kilograms): "))
rateofwaterconsumption = float(input("Enter the water consumption rate per day (in liters/day): "))
rateofoxygenconsumption = float(input("Enter the oxygen consumption rate per day (in liters/day): "))
rateoffoodconsumption = float(input("Enter the food consumption rate per day (in kilograms/day): "))
initial_resources = {'water': water, 'oxygen': oxygen, 'food': food}
consumption_rates = {'water': rateofwaterconsumption, 'oxygen': rateofoxygenconsumption, 'food': rateoffoodconsumption}
num_days = int(input("Enter the number of days over which you want to monitor consumption: "))
remaining_resources, low_resources = resourceusage(initial_resources, consumption_rates, num_days)

print("\nRemaining quantities of resources after", num_days, "days:")
for resource, quantity in remaining_resources.items():
    print(resource.capitalize() + ":", quantity)


if low_resources:
    print("\nWarning: The following resources are running low:")
    for resource in low_resources:
        print(resource.capitalize())

else:
    print("\nAll resources are sufficient.")
