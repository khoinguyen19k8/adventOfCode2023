import numpy as np
import pandas as pd


def batch_check(batch):
    for hand in batch.split(","):
        cubes_cnt, color = hand.strip().split()
        cubes_cnt = int(cubes_cnt)
        if (color == "red" and cubes_cnt > 12) or (color == "green" and cubes_cnt > 13) or (
                color == "blue" and cubes_cnt > 14):
            return False
    return True


def main(test_str, test=True):
    if not test:
        with open("input.txt") as f:
            input = f.read().split("\n")[:-1]
    else:
        input = test_str

    # print(input)
    # df = pd.DataFrame(0, index=np.arange(1, len(input) + 1), columns=["red", "blue", "green"])
    possible_games = []
    for idx, game in enumerate(input):
        possible_flag = True
        all_batches = game.split(":")[1].split(";")
        game_num = idx + 1
        for batch in all_batches:
            if batch_check(batch) is False:
                possible_flag = False
                break
        if possible_flag is True:
            possible_games.append(game_num)

    ids_sum = sum(possible_games)
    print(f"{ids_sum = }")


if __name__ == "__main__":
    test_str = "Game 7: 6 green, 6 red, 2 blue; 1 blue, 2 red, 7 green; 12 red; 5 green, 3 red, 1 blue; 16 red, 10 green"
    main(test_str, test=False)
