import os


def calculate_target_number(src, src_to_target_map):
    src_ranges, dest_starts = [], []
    for map_line in src_to_target_map.split(os.linesep)[1:]:
        if map_line: # Check for empty string
            dest_start, src_start, range_length = map(int, map_line.split())
            src_ranges.append(range(src_start, src_start + range_length))
            dest_starts.append(dest_start)
    for idx, src_rng in enumerate(src_ranges):
        if src in src_rng:
            return dest_starts[idx] + (src - src_rng[0])
    return src


def main():
    with open("input.txt") as f:
        input = f.read().split(os.linesep + os.linesep)
        # print(len(input), input[-1])
        all_src = [int(x) for x in input[0].split(":")[1].split()]
        all_maps = input[1:]
        for mp_instance in all_maps:
            all_src = [calculate_target_number(src, mp_instance) for src in all_src]
        print(min(all_src))


if __name__ == "__main__":
    main()
