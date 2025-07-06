from pgn.pgn_parse import get_player_results
from constants import DATA_FILE_PATH, PLAYER_NAME

results = get_player_results(DATA_FILE_PATH, PLAYER_NAME)

print(results)

with open("output/states.txt", "w") as f:
    for r in results:
        f.write(f"{r.name.lower()}\n")