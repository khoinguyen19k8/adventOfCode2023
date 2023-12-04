from collections import deque


def main():
    with open("input.txt") as f:
        all_cards = f.read().split("\n")[:-1]
        candidate_card_number = deque(range(len(all_cards)))
        total_scratch_cards = 0
        matching_numbers = []
        # Calculate matching numbers for each beforehand
        for card in all_cards:
            winning_numbers, owned_numbers = card.split(":")[1].split("|")
            intersected_numbers: set = set(winning_numbers.split()) & set(owned_numbers.split())
            matching_numbers.append(len(intersected_numbers))
        # Original/copies are treated the same as each instance is put into the deque and processed once.
        while len(candidate_card_number) > 0:
            card_number: int = candidate_card_number.pop()
            total_scratch_cards += 1
            candidate_card_number.extend(range(card_number + 1, card_number + matching_numbers[card_number] + 1))
    print(f"{total_scratch_cards = }")


if __name__ == "__main__":
    main()
