import re

def find_part_numbers(row: int, col: int, numbers: list[list[re.Match]]) -> int | None:
    for number in numbers[row]:
        if col in range(number.start(), number.end()):
            return int(number.group(0))
    return None


def calculate_gear_ratio(gear: re.Match, row: int, numbers: list[list[re.Match]]) -> int:
    start_row, end_row = row - 1, row + 1
    start_col, end_col = gear.start() - 1, gear.end()
    nbgh_part_numbers = []
    for row in range(start_row, end_row + 1): 
        for col in range(start_col, end_col + 1):
            candidate_part_number = find_part_numbers(row, col, numbers)
            if (candidate_part_number is not None) and (candidate_part_number not in nbgh_part_numbers):
                nbgh_part_numbers.append(candidate_part_number)
    if len(nbgh_part_numbers) == 2:
        print(f"row {row} gear: {nbgh_part_numbers[0]}, {nbgh_part_numbers[1]}")
        return nbgh_part_numbers[0] * nbgh_part_numbers[1]
    else:
        return 0


def main():
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]
        all_gears: list[list[re.Match]] = []
        all_numbers: list[list[re.Match]] = []
        gear_ratios_sum: int = 0
        for line in input:
            all_gears.append([gear for gear in re.finditer("\*", line)])
            all_numbers.append([number for number in re.finditer("[0-9]+", line)])
        for row, gear_row in enumerate(all_gears):
            for gear in gear_row:
                gear_ratios_sum += calculate_gear_ratio(gear, row, all_numbers)
    print(f"{gear_ratios_sum = }")
if __name__ == "__main__":
    main()