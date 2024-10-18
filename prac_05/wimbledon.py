def main():
    player_to_win = {}
    countries = []
    print("Wimbledon Champions:")
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        contents = in_file.readlines()[1:]
        for line in contents:
            record = line.strip().split(",")
            player_to_win[record[2]] = player_to_win.get(record[2], 0) + 1
            countries.append(record[1])
    for name, championships_won in player_to_win.items():
        print(name, championships_won)
    print()
    print(f"These {len(set(countries))} countries have won Wimbledon:")
    print(", ".join(sorted(set(countries))))


main()
