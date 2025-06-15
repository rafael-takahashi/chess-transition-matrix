from tabulate import tabulate

def print_tabulated(matrix: list[list[float]]):
    headers = ["FROM \\ TO", "WIN", "LOSS", "DRAW"]
    
    rows = [
        ["WIN"] + matrix[0],
        ["LOSS"] + matrix[1],
        ["DRAW"] + matrix[2],
    ]

    print(tabulate(rows, headers, floatfmt=".3f"))
