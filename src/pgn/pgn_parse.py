import chess.pgn
from constants import Color, Result

def get_player_results(file_path: str, player_name: str) -> list[str]:
    results = []

    with open(file_path) as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break

            player_color = Color.WHITE if game.headers.get("White", "?") == player_name else Color.BLACK
            result = game.headers.get("Result")

            match result:
                case "1-0":
                    if player_color == Color.WHITE: results.append(Result.WIN)
                    else: results.append(Result.LOSS)
                case "0-1":
                    if player_color == Color.WHITE: results.append(Result.LOSS)
                    else: results.append(Result.WIN)
                case "1/2-1/2":
                    results.append(Result.DRAW)

    return results
