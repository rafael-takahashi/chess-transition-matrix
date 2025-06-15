import os

PGN_FOLDER = "data/me"
OUTPUT_FILE = "data/me/merged_games.pgn"

def merge_pgns():
    pgn_files = [f for f in os.listdir(PGN_FOLDER) if f.endswith(".pgn")]

    with open(OUTPUT_FILE, "w", encoding="utf-8") as outfile:
        for filename in pgn_files:
            path = os.path.join(PGN_FOLDER, filename)
            with open(path, "r", encoding="utf-8") as infile:
                contents = infile.read().strip()
                outfile.write(contents + "\n\n")

    print(f"Merged {len(pgn_files)} PGN files into {OUTPUT_FILE}")

merge_pgns()
