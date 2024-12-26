import json
import random

def load_recipes(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []

def display_recipe(recipe):
    print("\n=== Recipe ===")
    print(f"Title: {recipe['title']}")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print("Steps:")
    for i, step in enumerate(recipe['steps'], start=1):
        print(f"{i}. {step}")

def save_favorite(recipe):
    try:
        with open('favorites.json', 'a') as file:
            file.write(json.dumps(recipe) + '\n')
        print("Recipe saved to favorites!")
    except Exception as e:
        print(f"Error saving favorite: {e}")

def show_favorites():
    try:
        with open('favorites.json', 'r') as file:
            print("\n=== Favorite Recipes ===")
            for line in file:
                recipe = json.loads(line)
                print(f"- {recipe['title']}")
    except FileNotFoundError:
        print("\nNo favorites found! Save some recipes first.")

def search_recipes(recipes, keyword):
    results = [recipe for recipe in recipes if keyword.lower() in ' '.join(recipe['ingredients']).lower()]
    if results:
        print(f"\nRecipes with '{keyword}':")
        for recipe in results:
            print(f"- {recipe['title']}")
    else:
        print(f"\nNo recipes found with '{keyword}'.")

def main():
    recipes = load_recipes('recipes.json')
    if not recipes:
        print("No recipes available. Please check your recipes.json file.")
        return

    while True:
        print("\n=== Recipe Randomizer Menu ===")
        print("1. Show a Random Recipe")
        print("2. View Favorite Recipes")
        print("3. Search Recipes by Ingredient")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()

        if choice == '1':
            random_recipe = random.choice(recipes)
            display_recipe(random_recipe)

            save = input("\nWould you like to save this recipe to your favorites? (y/n): ").strip().lower()
            if save == 'y':
                save_favorite(random_recipe)
            else:
                print("Okay! Enjoy cooking!")
        elif choice == '2':
            show_favorites()
        elif choice == '3':
            keyword = input("Enter an ingredient to search for: ").strip()
            search_recipes(recipes, keyword)
        elif choice == '4':
            print("Goodbye! Happy cooking!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()