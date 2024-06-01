import random

class Ship:
    def __init__(self, positions):
        self.positions = positions

def print_board(board):
    for row in board:
        print(" ".join(row))

def random_position():
    return random.randint(0, 5), random.randint(0, 5)

def check_valid_position(board, ship):
    for x, y in ship.positions:
        if x < 0 or x > 5 or y < 0 or y > 5 or board[y][x] != " ":
            return False
        for i in range(-1, 2):
            for j in range(-1, 2):
                if x + i >= 0 and x + i <= 5 and y + j >= 0 and y + j <= 5 and board[y + j][x + i] != " ":
                    return False
    return True

def place_ship(board, ship):
    for x, y in ship.positions:
        board[y][x] = "O"

def generate_ships():
    ships = []
    for _ in range(4):
        ship_positions = [(random_position())]
        while len(ship_positions) < 3:
            new_position = random_position()
            if all(abs(new_position[0] - x) > 1 or abs(new_position[1] - y) > 1 for x, y in ship_positions):
                ship_positions.append(new_position)
        ships.append(Ship(ship_positions))
    for _ in range(2):
        ship_positions = [(random_position())]
        while len(ship_positions) < 2:
            new_position = random_position()
            if all(abs(new_position[0] - x) > 1 or abs(new_position[1] - y) > 1 for x, y in ship_positions):
                ship_positions.append(new_position)
        ships.append(Ship(ship_positions))
    return ships

def main():
    player_board = [[" " for _ in range(6)] for _ in range(6)]
    computer_board = [[" " for _ in range(6)] for _ in range(6)]

    player_ships = generate_ships()
    computer_ships = generate_ships()

    for ship in player_ships:
        while not check_valid_position(player_board, ship):
            ship.positions = [(random_position())]
        place_ship(player_board, ship)

    for ship in computer_ships:
        while not check_valid_position(computer_board, ship):
            ship.positions = [(random_position())]
        place_ship(computer_board, ship)

    print("Player Board:")
    print_board(player_board)
    print("\nComputer Board:")
    print_board(computer_board)

if __name__ == "__main__":
    main()
