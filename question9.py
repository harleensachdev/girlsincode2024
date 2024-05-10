idealyield = 1000
idealsoilelements = 146.5
ideal_soil_quality = {"pH": 6.5, "nitrogen": 30, "phosphorus": 15, "potassium": 20}
ideal_climate_conditions = {"temperature": 25, "precipitation": 50}
userph = float(input("Enter pH level of the soil: "))
usernitrogen = float(input("Enter nitrogen content of the soil: "))
userphosphorus = float(input("Enter phosphorus content of the soil: "))
userpotassium = float(input("Enter potassium content of the soil: "))
usertemperature = float(input("Enter temperature (in Celsius): "))
userprecipitation = float(input("Enter precipitation (in mm): "))
sumofelements = userph+usernitrogen+userpotassium+userphosphorus+usertemperature+userprecipitation
newyield = idealyield * (sumofelements/idealsoilelements)
print("Yield will be {} hectares".format(newyield))