import random


def select_next_seed(seed_queue, cycle_count):
    for seed in seed_queue:
        file_size = seed.get_file_size()
        seed.priority = seed.exec_time * file_size

    seed_queue.sort(key=lambda s: s.priority)

    for i, seed in enumerate(seed_queue):
        if i == 0:
            seed.mark_favored()
        else:
            seed.unmark_favored()

    unused_seeds = [seed for seed in seed_queue if not seed.used_in_cycle]
    # All seeds have been used, start a new cycle
    if not unused_seeds:
        cycle_count += 1
        print(f"Starting a new cycle: {cycle_count}")
        for seed in seed_queue:
            # Reset usage for the new cycle
            seed.used_in_cycle = False
        unused_seeds = seed_queue

    favored_seeds = [seed for seed in seed_queue if seed.favored]
    non_favored_seeds = [seed for seed in seed_queue if not seed.favored]

    if random.random() < 0.8 and favored_seeds:  # 80% chance for favored
        selected = random.choice(favored_seeds)
    else:  # 20% chance for non-favored
        selected = (
            random.choice(non_favored_seeds) if non_favored_seeds else random.choice(unused_seeds)
        )

    selected.used_in_cycle = True
    return selected, cycle_count


# get the power schedule (# of new test inputs to generate for a seed)
def get_power_schedule(seed, avg_exec_time, avg_coverage):
    # AFL's implementation without depth and handicap
    exec_score = (
        300
        if seed.exec_time * 0.25 < avg_exec_time
        else (
            200
            if seed.exec_time * 0.5 < avg_exec_time
            else (
                150
                if seed.exec_time * 0.75 < avg_exec_time
                else (
                    100
                    if seed.exec_time < avg_exec_time
                    else 50 if seed.exec_time > avg_exec_time * 4 else 25
                )
            )
        )
    )
    coverage_score = (
        300
        if seed.coverage > avg_coverage * 1.5
        else (
            200
            if seed.coverage > avg_coverage
            else 150 if seed.coverage > avg_coverage * 0.75 else 100
        )
    )

    combined_score = exec_score + coverage_score
    # Limit the score to 10
    return max(1, min(int(combined_score / 10), 10))


def calculate_avg(total_exec_time, total_coverage, processed_seeds):
    if processed_seeds > 0:
        avg_exec_time = total_exec_time / processed_seeds
        avg_coverage = total_coverage / processed_seeds
    else:
        # Some default value
        avg_exec_time = 1000
        avg_coverage = 10

    return avg_exec_time, avg_coverage
