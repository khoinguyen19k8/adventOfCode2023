from collections import Counter
from argparse import ArgumentParser


def calculate_strength_hand(hand: str):
    """
    Return the strength of a hand in ascending order ranges from 0 -> 6.
    """
    match Counter(hand).most_common():
        case [(_, 5)]:  # Five of a kind
            return 0
        case [(_, 4), _]:  # Four of a kind
            return 1
        case [(_, 3), (_, 2)]:  # Full house
            return 2
        case [(_, 3), _, _]:  # Three of a kind
            return 3
        case [(_, 2), (_, 2), _]:  # Two pair
            return 4
        case [(_, 2), *_]:  # One pair
            return 5
        case _:  # High card
            return 6


def calculate_strength_card_type(hand: str):
    """
    Return the strength of a hand by card type.
    """
    all_types = ['A', 'K', 'Q', 'J', 'T', *range(9, 1, -1)]
    all_types = [str(x) for x in all_types]
    encoded_hand = [all_types.index(card) for card in hand]
    return encoded_hand


def main():
    parser = ArgumentParser()
    parser.add_argument("--input_file")
    args = parser.parse_args()
    with open(args.input_file) as f:
        input = f.read().split("\n")[:-1]
        hands_and_bids = [(line.split()[0], int(line.split()[1])) for line in input]
        hands_and_bids = sorted(
            sorted(hands_and_bids, key=lambda x: calculate_strength_card_type(x[0]), reverse=True),
            key=lambda x: calculate_strength_hand(x[0]), reverse=True
        )
        final_result = sum([i * bid for i, (hand, bid) in enumerate(hands_and_bids, 1)])
        print(f"{final_result = }")


if __name__ == "__main__":
    main()
