from pgn.pgn_parse import get_player_results
from constants import DATA_FILE_PATH, PLAYER_NAME
from markov import build_transition_matrix
from utils.output import print_tabulated

results = get_player_results(DATA_FILE_PATH, PLAYER_NAME)

transition_matrix = build_transition_matrix(results)

print_tabulated(transition_matrix)
