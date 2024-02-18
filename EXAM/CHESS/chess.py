import csv

def delta(player_1, player_2):
    return 1 / (1 + 2**((player_1 - player_2) / 100))

def read_players(filename):
    players = {}
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            players[row['PLAYER']] = int(row['SELO'])
    return players

def read_games(filename):
    games = []
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            games.append((row['PLAYER A'], row['PLAYER B'], row['RESULT']))
    return games

def update_selos(players, games):
    for player_a, player_b, result in games:
        score_a = players.get(player_a, 1500)
        score_b = players.get(player_b, 1500)
        if result == '1-0':
            delta_score = 200 * delta(score_a, score_b)
            players[player_a] = round(score_a + delta_score)
            players[player_b] = round(score_b - delta_score)
        elif result == '0-1':
            delta_score = 200 * delta(score_b, score_a)
            players[player_a] = round(score_a - delta_score)
            players[player_b] = round(score_b + delta_score)

def main():
    players = read_players('CHESS/players.csv')
    games = read_games('CHESS/games.csv')
    update_selos(players, games)
    sorted_players = sorted(players.items(), key=lambda x: x[1], reverse= True)
    for player, score in sorted_players:
        print(f"{player}: {score}")

if __name__ == "__main__":
    main()
