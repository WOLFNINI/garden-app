"""
Garden Advice Application - Improved Version
Provides seasonal gardening tips based on user-input month and hemisphere.
Refactored for better organization, reusability, and maintainability.
"""

def get_season(month: int, hemisphere: str = "Southern") -> str:
    """
    Determine the current season based on month and hemisphere.

    Args:
        month (int): Month number (1-12)
        hemisphere (str): 'Southern' or 'Northern' (default: Southern)

    Returns:
        str: Season name ('Summer', 'Autumn', 'Winter', 'Spring')
    """
    hemisphere = hemisphere.lower()

    if hemisphere == "southern":
        if month in [12, 1, 2]:
            return "Summer"
        elif month in [3, 4, 5]:
            return "Autumn"
        elif month in [6, 7, 8]:
            return "Winter"
        else:  # 9, 10, 11
            return "Spring"
    else:  # Northern Hemisphere (opposite seasons)
        if month in [6, 7, 8]:
            return "Summer"
        elif month in [9, 10, 11]:
            return "Autumn"
        elif month in [12, 1, 2]:
            return "Winter"
        else:  # 3, 4, 5
            return "Spring"


def get_gardening_tip(season: str) -> str:
    """
    Return gardening advice based on the season.

    Args:
        season (str): The season name

    Returns:
        str: Advice string for gardening
    """
    tips = {
        "Summer": "Water plants early morning or late afternoon. Great time for tomatoes, peppers, beans, and sunflowers!",
        "Autumn": "Plant winter vegetables like spinach, broccoli, cabbage. Start collecting leaves for compost.",
        "Winter": "Protect tender plants from frost with covers or mulch. Prune fruit trees and roses. Plan your spring garden.",
        "Spring": "Sow seeds directly outdoors. Fertilize beds and mulch well. Plant summer flowers and veggies now!"
    }
    return tips.get(season, "No specific advice available for this season.")


def display_advice(month: int, season: str, tip: str) -> None:
    """
    Display formatted gardening advice to the user.

    Args:
        month (int): Current month number
        season (str): Determined season
        tip (str): Gardening advice string
    """
    print("\n" + "=" * 50)
    print(f"Month: {month:02d}")
    print(f"Season: {season}")
    print("\nGardening Advice:")
    print(tip)
    print("=" * 50)


def main():
    """Main program: collect input and display gardening advice."""
    print("Welcome to the Improved Garden Advice App!")
    print("Tips are tailored for your hemisphere.\n")

    # Hemisphere selection
    while True:
        hemi_input = input("Southern or Northern Hemisphere? (S/N): ").strip().lower()
        if hemi_input in ['s', 'southern']:
            hemisphere = "Southern"
            break
        elif hemi_input in ['n', 'northern']:
            hemisphere = "Northern"
            break
        print("Please enter 'S' or 'N'.")

    # Month input with validation
    while True:
        try:
            month = int(input("Enter current month (1-12): "))
            if 1 <= month <= 12:
                break
            print("Month must be between 1 and 12.")
        except ValueError:
            print("Please enter a valid number.")

    # Get season and tip using separate functions
    season = get_season(month, hemisphere)
    tip = get_gardening_tip(season)

    # Display using dedicated function
    display_advice(month, season, tip)


if __name__ == "__main__":
    main()
