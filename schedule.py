import random


def select_next_seed(seed_queue):
    # this is a dummy implementation, it just randomly selects a seed
    # TODO: implement the "favor" feature of AFL
    for seed in seed_queue:
        file_size = seed.get_file_size()
        seed.priority = seed.exec_time * file_size
        
    seed_queue.sort(key=lambda s: s.priority)
    
    for i, seed in enumerate(seed_queue):
        if i == 0: 
            seed.mark_favored()
        else:
            seed.unmark_favored()
    
    favored_seeds = [seed for seed in seed_queue if seed.favored]
    non_favored_seeds = [seed for seed in seed_queue if not seed.favored]

    if random.random() < 0.8 and favored_seeds:  # 80% chance for favored
        return random.choice(favored_seeds)
    else:  # 20% chance for non-favored
        return random.choice(non_favored_seeds) if non_favored_seeds else random.choice(seed_queue)

    


# get the power schedule (# of new test inputs to generate for a seed)
def get_power_schedule(seed):
    # this is a dummy implementation, it just returns a random number
    # TODO: implement the power schedule similar to AFL (should consider the coverage, and execution time)
    return random.randint(1, 10)

