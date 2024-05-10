circumferenceofearth = 3.14 * 12742 * 1000
distancecoveredperstep = 0.5
distancecoveredeachminute = distancecoveredperstep *30
print("Steps taken are {}".format(round(circumferenceofearth/distancecoveredperstep)))
print("Duration is {} minutes".format(round(circumferenceofearth/distancecoveredeachminute)))

