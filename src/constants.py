from enum import Enum

DATA_FILE_PATH = "data/12312ASDASD12/merged_games.pgn"

PLAYER_NAME = "12312ASDASD12"

class Result(Enum):
    WIN = 0
    LOSS = 1
    DRAW = 2

class Color(Enum):
    WHITE = 0
    BLACK = 1
