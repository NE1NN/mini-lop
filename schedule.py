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
        selected = random.choice(non_favored_seeds) if non_favored_seeds else random.choice(unused_seeds)
    
    selected.used_in_cycle = True
    return selected, cycle_count

# get the power schedule (# of new test inputs to generate for a seed)
def get_power_schedule(seed):
    # this is a dummy implementation, it just returns a random number
    # TODO: implement the power schedule similar to AFL (should consider the coverage, and execution time)    
    score = seed.coverage / seed.exec_time
    normalized_score = min(max(int(score * 10), 1), 10)
    
    return max(1, normalized_score + random.randint(-1, 1))
