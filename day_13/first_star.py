from argparse import ArgumentParser
from numpy import matmul, flipud, trace
from numpy.linalg import norm
import numpy as np
from math import floor, ceil
import os

def calculate_cutoff_point(arr: np.ndarray):
    squared_norm = norm(arr, axis=1, ord=1)
    dp_leftover = matmul(arr, arr.T) - squared_norm
    for i in range(-dp_leftover.shape[0] + 2, dp_leftover.shape[0] - 1):
        diag_tmp = np.diag(np.flipud(dp_leftover), i)
        if len(diag_tmp) % 2 == 0 and sum(diag_tmp) == 0:
            if i <= 0:
                start, end = 0, len(diag_tmp) - 1
            else:
                start, end = i, arr.shape[0] - 1 
            cutoff_point = floor((start + end) / 2)
            return cutoff_point
    return None


def main():
    parser = ArgumentParser()
    parser.add_argument("--input_file")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    with open(args.input_file) as f:
        summarize = 0
        input = f.read().split(2 * os.linesep)
        for pattern in input:
            arr_str = [list(s.replace('.', '0').replace('#', '1')) for s in pattern.split(os.linesep) if s]
            arr_num = np.asarray(arr_str, dtype=np.int16)

            # Cutoff point for horizontal because norm across axis 1 is norm for each row.
            horizontal_cutoff_point = calculate_cutoff_point(arr_num)
            vertical_cutoff_point = calculate_cutoff_point(arr_num.T)
            if horizontal_cutoff_point:
                summarize += 100 * (horizontal_cutoff_point + 1)
            # Cutoff point for vertical because norm across axis 0 is norm for each column.
            elif vertical_cutoff_point:
                summarize += (vertical_cutoff_point + 1)
            else:
                summarize += 0
            print(f"{summarize = }")

if __name__ == "__main__":
    main()