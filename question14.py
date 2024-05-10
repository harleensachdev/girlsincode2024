
dishes_nutrition = {
    "Mac and Cheese": {"Calories": 376, "Protein": 9.7, "Fats": 16, "Fibre": 2.4},
    "Roast beef wrap": {"Calories": 606, "Protein": 30, "Fats": 33, "Fibre": 3.5},
    "Spinach omelette": {"Calories": 363, "Protein": 25, "Fats": 27, "Fibre": 1.3},
    "Chicken sandwich": {"Calories": 468, "Protein": 30, "Fats": 21, "Fibre": 2.6}
}


available_dishes = {
    "Mac and Cheese": 102,
    "Roast beef wrap": 207,
    "Spinach omelette": 259,
    "Chicken sandwich": 391
}
user_intake = {"Calories": 0, "Protein": 0, "Fats": 0, "Fibre": 0}
meal_categories = ["Breakfast", "Lunch", "Dinner"]
user_selections = {category: "" for category in meal_categories}
daily_essential_intake = {"Calories": 1200, "Protein": 50, "Fats": 50, "Fibre": 5}
def enough_food(meal):
    return available_dishes[meal] > 0
while True:
    for category in meal_categories:
        print(f"Available portions for {category}:")
        for meal, portions in available_dishes.items():
            print(f"{meal}: {portions}")
        meal_selection = input(f"Select a meal for your {category} (or type 'stop' to end): ")
        if meal_selection.lower() == "stop":
            break

        while meal_selection not in available_dishes or meal_selection in user_selections.values() or not enough_food(meal_selection):
            print("Sorry, this is not currently an option.")
            meal_selection = input(f"Select a meal for your {category} (or type 'stop' to end): ")

        user_selections[category] = meal_selection
        available_dishes[meal_selection] -= 1

        for nutrient, value in dishes_nutrition[meal_selection].items():
            user_intake[nutrient] += value

    if meal_selection.lower() == "stop":
        break
    if all(user_intake[nutrient] >= daily_essential_intake[nutrient] for nutrient in daily_essential_intake):
        print("Meal selections meet all daily intake requirements :) ")
    else:
        print("Meal selections do not meet the daily intake requirements, please rerun the program.")

print("Meal service ended.")
