# garden_advice.py
"""
Basic Gardening Advice Application
Provides seasonal gardening tips based on the current month.
Currently designed for Southern Hemisphere (e.g. South Africa).
"""

# Hardcoded value - will be replaced later
month = 7  # July (change this number to test different months)

# TODO: Replace the hardcoded month with user input
#       Example: month = int(input("Enter the current month (1-12): "))

# TODO: Add input validation to make sure month is between 1 and 12

# TODO: Create a separate function called get_season(month) that returns the season name
#       This will make the code cleaner and more reusable

# Determine season (Southern Hemisphere)
if month in [12, 1, 2]:
    season = "Summer"
    advice = "Water plants early in the morning or late afternoon. " \
             "Great time for tomatoes, peppers, beans, and sunflowers!"
elif month in [3, 4, 5]:
    season = "Autumn"
    advice = "Plant winter vegetables like spinach, broccoli, and cabbage. " \
             "Start collecting leaves for compost."
elif month in [6, 7, 8]:
    season = "Winter"
    advice = "Protect tender plants from frost with covers or mulch. " \
             "Prune fruit trees and roses. Good time to plan your spring garden."
else:  # 9, 10, 11
    season = "Spring"
    advice = "Sow seeds directly outdoors. Fertilize beds and mulch well. " \
             "Plant summer flowers and veggies now!"

# Display result
print(f"Month: {month}")
print(f"Season (Southern Hemisphere): {season}")
print("Gardening Advice:")
print(advice)

# TODO: Add docstrings to all future functions you create
# TODO: Make the program ask the user which hemisphere they are in
#       and adjust the season logic accordingly
# TODO: Replace the long if-elif chain with a dictionary or list-based approach
# TODO: Add more detailed, month-specific advice instead of just seasonal
# TODO: Handle invalid user input gracefully (e.g. show error message and ask again)
# TODO: (Advanced) Add weather API integration to give location-specific advice
