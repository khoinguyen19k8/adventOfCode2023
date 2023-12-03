import re

def match_letters(encoded_str, current_idx, letters_ls):
    if encoded_str[current_idx: current_idx + 3] in ["one", "two", "six"]:
        letter = encoded_str[current_idx: current_idx + 3]
        letters_in_num = str(letters_ls.index(letter) + 1)
        return letters_in_num
    elif encoded_str[current_idx: current_idx + 4] in ["four", "five", "nine"]:
        letter = encoded_str[current_idx: current_idx + 4]
        letters_in_num = str(letters_ls.index(letter) + 1)
        return letters_in_num
    elif encoded_str[current_idx: current_idx + 5] in ["three", "seven", "eight"]:
        letter = encoded_str[current_idx: current_idx + 5]
        letters_in_num = str(letters_ls.index(letter) + 1)
        return letters_in_num
    else:
        return encoded_str[current_idx]
def decode_calibration_value(amended_str: str) -> int:
    digits_ls = list(filter(lambda x: re.match(r"[0-9]", x), amended_str))
    decoded_value = int(''.join(digits_ls[0] + digits_ls[-1]))
    return decoded_value


def main():
    letters = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    acc_sum = 0
    with open("input.txt") as f:
        full_amended_list = f.read().split("\n")[:-1]
        for amended_str in full_amended_list:
            no_spelled_letters_str = ''.join([match_letters(amended_str, idx, letters) for idx in range(len(amended_str))])
            print(no_spelled_letters_str)
            acc_sum += decode_calibration_value(no_spelled_letters_str)
    print(f"{acc_sum = }")


if __name__ == "__main__":
    main()
