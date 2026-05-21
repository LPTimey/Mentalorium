from allocate import allocate_participant
import allocate


def matches_partial(person, target):

    # Group must match
    if person["group"] != target["group"]:
        return False

    # block1 must match EXACTLY (order-sensitive)
    if "block1" in target:
        if person["block1"] != target["block1"]:
            return False

    # block2 optional (order-sensitive)
    if "block2" in target:
        if person["block2"] != target["block2"]:
            return False

    return True


def find_seed_window(
    targets,
    window_size=30,
    seed_start=0,
    seed_end=100000
):

    for seed in range(seed_start, seed_end + 1):

        allocate.SEED = seed

        found = {}
        used_targets = set()

        for participant_id in range(window_size):

            person = allocate_participant(participant_id)

            for name, target in targets.items():

                if name in used_targets:
                    continue

                if matches_partial(person, target):

                    found[name] = participant_id
                    used_targets.add(name)

        if len(found) == len(targets):

            return {
                "seed": seed,
                "window_size": window_size,
                "matches": found
            }

    return None


# -------------------------
# TARGET DEFINITIONS
# -------------------------

targets = {
    "VJ": {
        "group": "Active",
        "block1": [
            ("Amina", "Incorrect"),
            ("Aylin", "Correct"),
            ("Lena", "Incorrect")
        ]
    },

    "Sina": {
        "group": "Control",
        "block1": [
            ("Lena", "Incorrect"),
            ("Martina", "Correct"),
            ("Mathias", "Incorrect")
        ]
    }
}


# -------------------------
# RUN SEARCH
# -------------------------

result = find_seed_window(
    targets=targets,
    window_size=30,
    seed_start=0,
    seed_end=100000
)

print(result)