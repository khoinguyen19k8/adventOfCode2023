import re
from math import sqrt, ceil
def main():
    """
    Solving the inequality (total - x) * x > record
    -> -sqrt(1/4 * (total ** 2) - record) + total/2 < x < sqrt(1/4 * (total ** 2) - record) + total/2
    Number of integers between two real numbers:
    https://math.stackexchange.com/questions/1867236/number-of-integers-between-two-real-numbers
    """
    final_result = 1
    with open("input.txt") as f:
        time_allow, record_distances = [re.split(" +", line)[1:] for line in f.read().split("\n")[:-1]]
        time_allow, record_distances = [int(t) for t in time_allow], [int(d) for d in record_distances]
        for total, record in zip(time_allow, record_distances):
            tmp = sqrt((1/4) * (total ** 2) - record)
            left = -tmp + (total / 2)
            right = tmp + (total / 2)
            number_of_ways = (ceil(right) - ceil(left))
            number_of_ways = number_of_ways - 1 if right.is_integer() else number_of_ways
            final_result *= number_of_ways
    print(f"{final_result = }")


if __name__ == "__main__":
    main()
