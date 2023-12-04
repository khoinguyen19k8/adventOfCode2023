def main():
    acc_sum = 0
    with open("input.txt") as f:
        input = f.read().split("\n")[:-1]
        for card in input:
            winning_numbers, owned_numbers = card.split(":")[1].split("|")
            matching_numbers = set(winning_numbers.split()) & set(owned_numbers.split())
            acc_sum += 2 ** (len(matching_numbers) - 1) if len(matching_numbers) >= 1 else 0
    print(f"{acc_sum = }")


if __name__ == "__main__":
    main()
