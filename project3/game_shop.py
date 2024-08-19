from game import Game

class GameShop:
    def __init__(self):
        self.games = [
            Game("The Legend of Zelda", 59.99),
            Game("Super Mario Odyssey", 49.99),
            Game("Real Minecraft", 19.99),
            Game("Free Fortnite", 0.00),
            Game("Cyberpunk 2077", 39.99)
        ]
        self.cart = []

    def display_games(self):
        print("Available games:")
        for index, game in enumerate(self.games):
            print(f"{index + 1}. {game.name} - ${game.price:.2f}")

    def add_to_cart(self, game_index, quantity):
        game = self.games[game_index]
        self.cart.append((game, quantity))
        print(f"Added {quantity} x {game.name} to cart.")

    def calculate_total(self):
        total = 0
        for game, quantity in self.cart:
            total += game.price * quantity
        return total

    def checkout(self):
        if not self.cart:
            print("Your cart is empty.")
        else:
            print("Your cart:")
            for game, quantity in self.cart:
                print(f"{quantity} x {game.name} - ${game.price * quantity:.2f}")
            total = self.calculate_total()
            print(f"The Total Cost is ${total:.2f}")
