import os
from argparse import ArgumentParser
from collections import deque
import re
from math import gcd
from functools import reduce


def return_instruction(node, nodes_map, nav):
    if nav == 'L':
        return nodes_map[node][0]
    elif nav == 'R':
        return nodes_map[node][1]


def find_number_of_steps(starting_node, nodes_map, forward_queue):
    count = 0
    while not starting_node.endswith('Z'):
        count += 1
        movement = forward_queue.popleft()
        starting_node = return_instruction(starting_node, nodes_map, movement)
        forward_queue.append(movement)
    return count


def main():
    parser = ArgumentParser()
    parser.add_argument("--input_file")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    with (open(args.input_file) as f):
        instructions, nodes_and_instructions = f.read().split(os.linesep + os.linesep)
        nodes_and_instructions = nodes_and_instructions.split(os.linesep)[:-1]
        forward_queue = deque(instructions)
        nodes_map, all_nodes = {}, []
        for node_line in nodes_and_instructions:
            n, rest = node_line.split(" = ")
            nodes_map[n] = (*re.findall(r"\w+", rest),)
            all_nodes.append(n)

        forward_nodes = list(filter(lambda x: x.endswith('A'), all_nodes))
        steps_required = [find_number_of_steps(node, nodes_map, forward_queue.copy()) for node in forward_nodes]
        steps_required = reduce(lambda x, y: int(abs(x * y) / gcd(x, y)), steps_required)
        print(f"{steps_required = }")



if __name__ == "__main__":
    main()
