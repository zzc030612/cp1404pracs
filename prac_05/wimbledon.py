def main():
    """Print countries and championship winners."""
    player_to_win = {}
    winning_countries = []
    print("Wimbledon Champions:")
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        contents = in_file.readlines()[1:]
        process_contents_of_file(contents, winning_countries, player_to_win)
    print_championship_winners(player_to_win)
    print()
    print_countries(winning_countries)


def process_contents_of_file(contents, countries, player_to_win):
    """Process the contents of a file into two variables."""
    for line in contents:
        # line: 1968,AUS,Rod Laver,AUS,Tony Roche,"6–3, 6–4, 6–2\n"
        record = line.strip().split(",")
        player_to_win[record[2]] = player_to_win.get(record[2], 0) + 1
        countries.append(record[1])


def print_championship_winners(player_to_win):
    """Print championship winners names and amount won."""
    for name, championships_won in player_to_win.items():
        print(name, championships_won)


def print_countries(countries):
    """Print countries names that has won an championship."""
    unique_countries = set(countries)
    print(f"These {len(unique_countries)} countries have won Wimbledon:")
    print(", ".join(sorted(unique_countries)))


main()
