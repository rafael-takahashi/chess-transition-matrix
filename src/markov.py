import numpy as np
from constants import Result

def count_transitions(data: list[Result]) -> np.ndarray:
    n = len(Result)
    counts = np.zeros((n, n), dtype=int)

    for i in range(len(data) - 1):
        from_state = data[i].value
        to_state = data[i + 1].value
        counts[from_state, to_state] += 1

    return counts

def build_transition_matrix(data: list[Result]) -> np.ndarray:
    counts = count_transitions(data)
    row_sums = counts.sum(axis=1, keepdims=True)

    with np.errstate(divide='ignore', invalid='ignore'):
        transition_matrix = counts / row_sums
        transition_matrix[np.isnan(transition_matrix)] = 0

    transition_matrix = np.floor(transition_matrix * 1000) / 1000

    return transition_matrix
