from game_shop import GameShop

def main():
    shop = GameShop()

    while True:
        shop.display_games()
        choice = input("Enter the number of the game you want to buy (or 'q' to quit): ")

        if choice.lower() == 'q':
            break

        try:
            game_index = int(choice) - 1
            if game_index < 0 or game_index >= len(shop.games):
                print("Invalid choice. Please try again.")
                continue

            quantity = int(input(f"How many copies of {shop.games[game_index].name} would you like to buy? "))
            if quantity <= 0:
                print("Quantity must be positive. Please try again.")
                continue

            shop.add_to_cart(game_index, quantity)
        except ValueError:
            print("Invalid input. Please enter a number.")

    shop.checkout()

if __name__ == "__main__":
    main()
