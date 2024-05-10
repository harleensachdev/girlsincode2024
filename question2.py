
current_velocity = float(input("Enter the current velocity of the lunar lander (in meters per second): "))
safe_velocity = 2
if current_velocity <= safe_velocity:
    print("It's safe to land.")
else:
    print("It's not safe to land. Decrease your velocity.")
