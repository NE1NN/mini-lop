import random


def select_next_seed(seed_queue):
    for seed in seed_queue:
        file_size = seed.get_file_size()
        seed.priority = seed.exec_time * file_size

    seed_queue.sort(key=lambda s: s.priority)

    for i, seed in enumerate(seed_queue):
        if i < len(seed_queue) // 2:
            seed.mark_favored()
        else:
            seed.unmark_favored()

    unused_seeds = [seed for seed in seed_queue if not seed.used_in_cycle]
    # All seeds have been used, start a new cycle
    if not unused_seeds:
        for seed in seed_queue:
            # Reset usage for the new cycle
            seed.used_in_cycle = False
        unused_seeds = seed_queue

    favored_seeds = [seed for seed in unused_seeds if seed.favored]
    non_favored_seeds = [seed for seed in unused_seeds if not seed.favored]

    if random.random() < 0.8 and favored_seeds:  # 80% chance for favored
        selected = random.choice(favored_seeds)
    else:  # 20% chance for non-favored
        selected = (
            random.choice(non_favored_seeds) if non_favored_seeds else random.choice(unused_seeds)
        )

    selected.used_in_cycle = True
    return selected


# get the power schedule (# of new test inputs to generate for a seed)
def get_power_schedule(seed, avg_exec_time, avg_coverage):
    # AFL's implementation without depth and handicap
    HAVOC_MAX_MULT = 16
    perf_score = 0

    if seed.exec_time * 0.1 > avg_exec_time:
        perf_score = 10
    elif seed.exec_time * 0.25 > avg_exec_time:
        perf_score = 25
    elif seed.exec_time * 0.5 > avg_exec_time:
        perf_score = 50
    elif seed.exec_time * 0.75 > avg_exec_time:
        perf_score = 75
    elif seed.exec_time * 4 < avg_exec_time:
        perf_score = 300
    elif seed.exec_time * 3 < avg_exec_time:
        perf_score = 200
    elif seed.exec_time * 2 < avg_exec_time:
        perf_score = 150

    if seed.coverage * 0.3 > avg_coverage:
        perf_score *= 3
    elif seed.coverage * 0.5 > avg_coverage:
        perf_score *= 2
    elif seed.coverage * 0.75 > avg_coverage:
        perf_score *= 1.5
    elif seed.coverage * 3 < avg_coverage:
        perf_score *= 0.25
    elif seed.coverage * 2 < avg_coverage:
        perf_score *= 0.5
    elif seed.coverage * 1.5 < avg_coverage:
        perf_score *= 0.75

    if perf_score > HAVOC_MAX_MULT * 100:
        perf_score = HAVOC_MAX_MULT * 100

    return int(perf_score)


def calculate_avg(total_exec_time, total_coverage, processed_seeds):
    if processed_seeds > 0:
        avg_exec_time = total_exec_time / processed_seeds
        avg_coverage = total_coverage / processed_seeds
    else:
        # Some default value
        avg_exec_time = 1000
        avg_coverage = 10

    return avg_exec_time, avg_coverage
