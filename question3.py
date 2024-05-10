import numpy as np

def displacementofcannon(initialvelocity, angle, time):
    gravityofmars = 3.71
    minradians = np.deg2rad(m)
    finaldisplacement = initialvelocity * time * np.cos(minradians) - 0.5 * gravityofmars * t**2

    return finaldisplacement
u = 200
t = 90
m = 87

displacement = displacementofcannon(u, m, t)
print("Displacement of the cannon:", displacement, "m")
