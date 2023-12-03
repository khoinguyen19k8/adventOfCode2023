import numpy as np
import pandas as pd
from functools import reduce


def fill_color(batch, batch_num, df):
    for hand in batch.split(","):
        cubes_cnt, color = hand.strip().split()
        cubes_cnt = int(cubes_cnt)
        df.loc[batch_num, color] = cubes_cnt


def main(test_str, test=True):
    if not test:
        with open("input.txt") as f:
            input = f.read().split("\n")[:-1]
    else:
        input = test_str

    final_result = 0
    for game in input:
        all_batches: list = game.split(":")[1].split(";")
        all_batches_df = pd.DataFrame(0, index=np.arange(1, len(all_batches) + 1), columns=["red", "blue", "green"])
        for batch_num, batch in enumerate(all_batches, 1):
            fill_color(batch, batch_num, all_batches_df)

        cubes_power = reduce(lambda x, y: x*y, list(all_batches_df.max()))
        final_result += cubes_power

    print(f"{final_result = }")


if __name__ == "__main__":
    test_str = "Game 7: 6 green, 6 red, 2 blue; 1 blue, 2 red, 7 green; 12 red; 5 green, 3 red, 1 blue; 16 red, 10 green"
    main(test_str, test=False)
