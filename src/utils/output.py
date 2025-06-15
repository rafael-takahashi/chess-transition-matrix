from tabulate import tabulate
import numpy as np
from constants import Result

def print_tabulated(matrix: np.ndarray):
    headers = ["FROM \\ TO"] + [r.name for r in Result]
    
    rows = []
    for i, from_state in enumerate(Result):
        row = [from_state.name] + list(matrix[i])
        rows.append(row)

    print(tabulate(rows, headers, floatfmt=".3f"))
