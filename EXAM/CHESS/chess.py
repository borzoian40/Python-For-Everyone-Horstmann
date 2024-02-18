FILENAME = "players.csv"
GAMES    = "games.csv" 

def delta(player_1, player_2):
    return 1 / (1 + 2**((player_1 - player_2) / 100))

def read_players(filepath):
    players = {}
    try:
        with open(filepath, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name, rating = row.strip().split()
                players[name] = rating


    except FileNotFoundError:
        print("We didn't file find your file! Now that's a big problem")

    return players

def main():
    chess_players = read_players(FILENAME)

    print(chess_players)


if __name__ == "__main__":
    main()