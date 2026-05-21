import random
import sys

SEED = 403

CASES = ["Amina", "Aylin", "Lena", "Martina", "Mathias"]

def build_block(rng, cases):

    correct_index = rng.randint(0, 2)

    block = []

    for i, case in enumerate(cases):

        truth = "Correct" if i == correct_index else "Incorrect"

        block.append((case, truth))

    rng.shuffle(block)

    return block


def allocate_participant(n):

    rng = random.Random(f"{SEED}-{n}")

    # Group assignment
    group = rng.choice(["Active", "Control"])

    # Shared case
    shared = rng.choice(CASES)

    # Remaining cases
    remaining = [c for c in CASES if c != shared]

    rng.shuffle(remaining)

    block1_cases = [shared] + remaining[:2]
    block2_cases = [shared] + remaining[2:]

    rng.shuffle(block1_cases)
    rng.shuffle(block2_cases)

    block1 = build_block(rng, block1_cases)
    block2 = build_block(rng, block2_cases)

    return {
        "group": group,
        "block1": block1,
        "block2": block2
    }

def print_csv_header():
    print("group,Case11,Correct11,Case12,Correct12,Case13,Correct13,Case21,Correct21,Case22,Correct22,Case23,Correct23")

def print_csv_row(person):
    print(
        f'{person["group"]},'
        f'{person["block1"][0][0]},{person["block1"][0][1]},'
        f'{person["block1"][1][0]},{person["block1"][1][1]},'
        f'{person["block1"][2][0]},{person["block1"][2][1]},'
        f'{person["block2"][0][0]},{person["block2"][0][1]},'
        f'{person["block2"][1][0]},{person["block2"][1][1]},'
        f'{person["block2"][2][0]},{person["block2"][2][1]}'
    )

def usage():

    print("Usage:")
    print("  python allocate.py 5")
    print("  python allocate.py 1-10")

def main():

    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    arg = sys.argv[1]

    print_csv_header();

    # Single participant
    if "-" not in arg:

        try:
            n = int(arg)
        except ValueError:
            usage()
            sys.exit(1)

        participant = allocate_participant(n)
        print_csv_row(participant)
        return

    # Range of participants
    try:
        start, end = arg.split("-")
        start = int(start)
        end = int(end)
    except ValueError:
        usage()
        sys.exit(1)

    if start > end:
        print("Error: start must be <= end")
        sys.exit(1)

    for n in range(start, end + 1):

        participant = allocate_participant(n)

        print_csv_row(participant)


if __name__ == "__main__":
    main()