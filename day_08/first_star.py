import os
from argparse import ArgumentParser
from collections import deque
import ast
import re


def main():
    parser = ArgumentParser()
    parser.add_argument("--input_file")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    with open(args.input_file) as f:
        instructions, nodes = f.read().split(os.linesep + os.linesep)
        nodes = nodes.split(os.linesep)[:-1]
        instructions_queue = deque(instructions)
        steps_required = 0
        nodes_map = {}

        for node_line in nodes:
            n, rest = node_line.split(" = ")
            # print(f"{n = }, {rest = }")
            nodes_map[n] = (*re.findall("\w+", rest),)
        # print(f"{nodes_map = }, {instructions_queue = }")
        current_node = "AAA"
        while current_node != "ZZZ":
            movement = instructions_queue.popleft()
            # print(f"{current_node = }, {movement = }")
            steps_required += 1
            if movement == 'L':
                current_node = nodes_map[current_node][0]
            elif movement == 'R':
                current_node = nodes_map[current_node][1]
            instructions_queue.append(movement)
        print(f"{steps_required = }")


if __name__ == "__main__":
    main()
