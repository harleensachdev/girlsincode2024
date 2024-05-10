
meals = [
    {"meal": "Pasta", "date": "2024-03-12"},
    {"meal": "Spaghetti", "date": "2024-03-01"},
    {"meal": "Vegetable Fry", "date": "2024-03-05"},
    {"meal": "Beef Burger", "date": "2024-03-08"},
    {"meal": "Chicken Curry", "date": "2024-03-03"},
    {"meal": "Grilled peas", "date": "2024-03-10"},
    {"meal": "Tofu Stir Fry", "date": "2024-03-15"},
    {"meal": "Vegetarian Chili", "date": "2024-03-20"},
    {"meal": "Shrimp Scampi", "date": "2024-03-18"},
    {"meal": "Beef Tacos", "date": "2024-03-22"},
    {"meal": "Chicken Alfredo", "date": "2024-03-25"},
    {"meal": "Vegetable Lasagna", "date": "2024-03-30"},
    {"meal": "Margherita Pizza", "date": "2024-03-31"},
    {"meal": "Eggplant Parmesan", "date": "2024-03-27"}
]

sorted_meals = sorted(meals, key=lambda x: x["date"])
print("Organised meals in ascending order of expiry date:")
for meal in sorted_meals:
    print(f"{meal['date']}: {meal['meal']}")
