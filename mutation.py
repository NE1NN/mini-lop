import random

def splice_mutation(conf, seed, seed_queue):
    if len(seed_queue) < 2:
        return havoc_mutation(conf, seed) 

    # Select another seed randomly, ensuring it's not the same as the current seed
    other_seed = random.choice([s for s in seed_queue if s.seed_id != seed.seed_id])

    with open(seed.path, "rb") as f1, open(other_seed.path, "rb") as f2:
        data1 = bytearray(f1.read())
        data2 = bytearray(f2.read())

    len1, len2 = len(data1), len(data2)

    # Choose random splice points for both seeds
    splice_point1 = random.randint(1, len1 - 1) if len1 > 1 else 0
    splice_point2 = random.randint(1, len2 - 1) if len2 > 1 else 0

    spliced_data = data1[:splice_point1] + data2[splice_point2:]

    # Apply havoc mutation on the spliced file
    data = havoc_mutation_operation(spliced_data)
    save_to_input(conf, data)


def havoc_mutation(conf, seed):
    with open(seed.path, "rb") as f:
        data = bytearray(f.read())

    data = havoc_mutation_operation(data)
    save_to_input(conf, data)

def add_random_value(data):
    data_len = len(data)
    
    size = random.choice([2, 4, 8])
    if data_len < size:
        return data
    position = random.randint(0, data_len - size)

    selected_bytes = data[position : position + size]
    value = int.from_bytes(selected_bytes, byteorder="little", signed=True)
    mutated_value = value + random.randint(-100, 100)  # Add/sub random value

    min_value = -(2 ** (size * 8 - 1))
    max_value = 2 ** (size * 8 - 1) - 1
    mutated_value = max(min_value, min(max_value, mutated_value))

    mutated_bytes = mutated_value.to_bytes(size, byteorder="little", signed=True)
    data[position : position + size] = mutated_bytes
    
    return data

def replace_byte(data):
    data_len = len(data)
    
    size = random.choice([2, 4, 8])
    if data_len < size:
        return data
    position = random.randint(0, data_len - size)

    # Replace with interesting values
    interesting_values = [0, -1, 1, 2 ** (size * 8 - 1) - 1, -(2 ** (size * 8 - 1))]
    value = random.choice(interesting_values)
    mutated_bytes = value.to_bytes(size, byteorder="little", signed=True)
    data[position : position + size] = mutated_bytes
    
    return data

def replace_chunk(data):
    data_len = len(data)
    
    if data_len < 2:
        return data
    chunk_len = random.randint(1, data_len // 2)  # Random chunk length
    pos1 = random.randint(0, data_len - chunk_len)
    pos2 = random.randint(0, data_len - chunk_len)
    chunk1 = data[pos1 : pos1 + chunk_len]
    data[pos2 : pos2 + chunk_len] = chunk1

def havoc_mutation_operation(data):    
    data = add_random_value(data)
    data = replace_byte(data)
    data = replace_chunk(data)
    return data
    

def save_to_input(conf, data):
    with open(conf["current_input"], "wb") as f_out:
        f_out.write(data)