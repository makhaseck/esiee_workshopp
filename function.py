def cook_spaghetti_bolognese(servings=2, vegetarian=False, spicy=False):
    def prepare_ingredients():
        ingredients = ['onions', 'garlic', 'carrots', 'tomato sauce']
        if not vegetarian:
            ingredients.append('minced beef')
        else:
            ingredients.append('lentils')
        if spicy:
            ingredients.append('chili peppers')

        print("Preparing ingredients...")
        for item in ingredients:
            if item == 'carrots':
                print("Skipping carrots because someone doesn’t like them 😅")
                continue  # Skip carrots (just as an example)
            print(f"Chopping {item}...")

        print("Water is boiling for spaghetti...")

    def cook_sauce():
        print("Starting sauce...")
        print("Sautéing onions and garlic...")
        
        if not vegetarian:
            print("Adding and browning minced beef...")
        else:
            print("Lentils are being cooked...")

        # Placeholder for a more complex spice mix step later
        print("Checking spices...")
        pass  # Nothing happens yet, to be implemented later

        print("Adding tomato sauce...")
        if spicy:
            print("Adding chili peppers...")
        print("Simmering sauce for 20 minutes...")

    def cook_pasta():
        print(f"Cooking spaghetti ({servings * 100}g)...")
        print("Draining and saving some pasta water...")

    def serve():
        print("Mixing pasta and sauce...")
        if vegetarian:
            print("Topping with fresh basil 🌿")
        else:
            print("Topping with grated parmesan 🧀")
        print(f"🍝 Dish ready for {servings} serving(s)! Enjoy!")

    # Main flow
    print("👨‍🍳 Starting to cook Spaghetti Bolognese...\n")
    prepare_ingredients()
    print()
    cook_sauce()
    print()
    cook_pasta()
    print()
    serve()

# Run it
cook_spaghetti_bolognese(servings=3, vegetarian=True, spicy=True)
