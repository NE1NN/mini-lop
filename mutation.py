import random


def splice_mutation(conf, seed, seed_queue):
    # Ensure there is at least one other seed to splice with
    if len(seed_queue) < 2:
        return havoc_mutation(conf, seed)  # Fallback to havoc if not enough seeds

    # Select another seed randomly, ensuring it's not the same as the current seed
    other_seed = random.choice([s for s in seed_queue if s.seed_id != seed.seed_id])

    # Read both seeds
    with open(seed.path, "rb") as f1, open(other_seed.path, "rb") as f2:
        data1 = bytearray(f1.read())
        data2 = bytearray(f2.read())

    len1, len2 = len(data1), len(data2)

    # Choose random splice points for both seeds
    splice_point1 = random.randint(1, len1 - 1) if len1 > 1 else 0
    splice_point2 = random.randint(1, len2 - 1) if len2 > 1 else 0

    # Combine the first half of the first seed with the second half of the second seed
    spliced_data = data1[:splice_point1] + data2[splice_point2:]

    # Save the spliced data temporarily to the `current_input` file
    with open(conf["current_input"], "wb") as f:
        f.write(spliced_data)

    # Apply havoc mutation on the spliced file
    havoc_mutation(conf, seed)

def havoc_mutation(conf, seed):
    # this is a dummy implementation, it just randomly flips some bytes
    # TODO: implement the havoc mutation similar to AFL
    with open(seed.path, "rb") as f:
        data = bytearray(f.read())

        data_len = len(data)

        for _ in range(random.randint(1, data_len)):
            mutation_type = random.choice(["bit_flip", "add_sub", "replace_value", "replace_chunk"])

            if mutation_type == "bit_flip":
                # Flip a random bit in the data
                byte_idx = random.randint(0, data_len - 1)
                bit_idx = random.randint(0, 7)
                data[byte_idx] ^= 1 << bit_idx

            elif mutation_type == "add_sub":
                # Add or subtract a random value to/from a byte
                byte_idx = random.randint(0, data_len - 1)
                data[byte_idx] = (data[byte_idx] + random.choice([-1, 1])) % 256

            elif mutation_type == "replace_value":
                # Replace a byte with an interesting value
                byte_idx = random.randint(0, data_len - 1)
                interesting_values = [0x00, 0xFF, 0x7F, 0x80, 0x01]
                data[byte_idx] = random.choice(interesting_values)

            elif mutation_type == "replace_chunk":
                # Replace a random chunk with another chunk
                if data_len > 1:
                    start_idx = random.randint(0, data_len - 2)
                    end_idx = random.randint(start_idx + 1, data_len - 1)
                    chunk_len = end_idx - start_idx
                    chunk = data[start_idx:end_idx]
                    insert_idx = random.randint(0, data_len - chunk_len)
                    data[insert_idx : insert_idx + chunk_len] = chunk

        # write the mutated data back to the current input file
        with open(conf["current_input"], "wb") as f_out:
            f_out.write(data)
