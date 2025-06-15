import math
from constants import Result

def count_transitions(data: list[Result]) -> dict[tuple[Result, Result], int]:
    counts = {}

    for i in range(len(data) - 1):
        pair = (data[i], data[i + 1])
        counts[pair] = counts.get(pair, 0) + 1

    return counts

def build_transition_matrix(data: list[Result]) -> list[list[float]]:
    counts = count_transitions(data)

    n = len(Result)
    transition_matrix = [[0] * n for _ in range(n)]

    for (from_state, to_state), count in counts.items():
        transition_matrix[from_state.value][to_state.value] = count
    
    for i in range(n):
        row_sum = sum(transition_matrix[i])
        transition_matrix[i] = [
            math.trunc((count / row_sum) * 1000) / 1000
            for count in transition_matrix[i]
        ]

    return transition_matrix
