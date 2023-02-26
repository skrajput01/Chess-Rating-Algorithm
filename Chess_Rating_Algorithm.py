### SKR - Chess Rating Algorithm [26/02/2023]
# Compares 2 Chess players using the ELO rating system and changes player ratings based on the outcome of their game. If a player wins a game, their rating increases, and if they lose a game, their rating decreases. Chess players are given a base rating of 1500.


# Defines a Player class to store the rating of each player
class Player:
    def __init__(self, rating):
        self.rating = rating

# Defines an Elo class that contains the logic for calculating the expected score and updating the ratings of the players
class Elo:
    # Defines a constant K that determines the sensitivity of the ratings to changes
    K = 32

    # Defines a static method that calculates the expected score of a player against an opponent based on their ratings
    @staticmethod
    def expected_score(player, opponent):
        return 1 / (1 + 10 ** ((opponent.rating - player.rating) / 400))

    # Defines a static method that updates the ratings of the players based on the actual result of the game
    @staticmethod
    def update(player1, player2):
        result = int(input("Enter the result of the game (0 for draw, 1 for player 1 win, 2 for player 2 win): "))
        # Determines the actual scores for each player based on the outcome of the game
        if result == 1:
            actual1, actual2 = 1, 0
        elif result == 2:
            actual1, actual2 = 0, 1
        else:
            actual1, actual2 = 0.5, 0.5
        # Calculates the expected scores for each player based on their ratings and the opponent's rating
        expected1 = Elo.expected_score(player1, player2)
        expected2 = Elo.expected_score(player2, player1)
        # Updates the ratings of each player based on the actual and expected scores
        player1.rating += Elo.K * (actual1 - expected1)
        player2.rating += Elo.K * (actual2 - expected2)

# Creates two players with different ratings (adjust values depending on the player)
player1 = Player(1500)
player2 = Player(1000)
Elo.update(player1, player2)
# Prints the updated ratings for each player using the `print` statement
print(f"Player 1 rating: {player1.rating}")
print(f"Player 2 rating: {player2.rating}")
