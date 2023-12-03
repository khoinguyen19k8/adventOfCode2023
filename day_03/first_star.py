import re

def check_neighborhood(number: re.Match, row_num: int, schematic_matrix: list) -> bool:
    start_row, end_row = row_num - 1, row_num + 1
    start_col, end_col = number.start() - 1, number.end()
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            try:
                if re.match("[^0-9^\..]", schematic_matrix[row][col]) is not None:
                    return True
            except IndexError as e:
                pass
    return False

def main():
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]
        engine_sum = 0
        valid_part_num = []
        for row_num, line in enumerate(input):
            all_numbers = re.finditer("[0-9]+", line)
            for number_obj in all_numbers:
                if check_neighborhood(number_obj, row_num, input) is True:
                    valid_part_num.append(number_obj.group(0))
                    engine_sum += int(number_obj.group(0))
    with open("output.txt", "w") as f:
        f.write('\n'.join(valid_part_num))
    print(f"{engine_sum = }")

    pass
if __name__ == "__main__":
    main()