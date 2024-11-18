import random


def havoc_mutation(conf, seed):
    # this is a dummy implementation, it just randomly flips some bytes
    # TODO: implement the havoc mutation similar to AFL
    with open(seed.path, 'rb') as f:
        data = bytearray(f.read())

        data_len = len(data)

        for _ in range(random.randint(1, data_len)):
            mutation_type = random.choice(['bit_flip', 'add_sub', 'replace_value', 'replace_chunk'])
            
            if mutation_type == 'bit_flip':
                # Flip a random bit in the data
                byte_idx = random.randint(0, data_len - 1)
                bit_idx = random.randint(0, 7)
                data[byte_idx] ^= (1 << bit_idx)
            
            elif mutation_type == 'add_sub':
                # Add or subtract a random value to/from a byte
                byte_idx = random.randint(0, data_len - 1)
                data[byte_idx] = (data[byte_idx] + random.choice([-1, 1])) % 256
            
            elif mutation_type == 'replace_value':
                # Replace a byte with an interesting value
                byte_idx = random.randint(0, data_len - 1)
                interesting_values = [0x00, 0xFF, 0x7F, 0x80, 0x01]
                data[byte_idx] = random.choice(interesting_values)
            
            elif mutation_type == 'replace_chunk':
                # Replace a random chunk with another chunk
                if data_len > 1:
                    start_idx = random.randint(0, data_len - 2)
                    end_idx = random.randint(start_idx + 1, data_len - 1)
                    chunk_len = end_idx - start_idx
                    chunk = data[start_idx:end_idx]
                    insert_idx = random.randint(0, data_len - chunk_len)
                    data[insert_idx:insert_idx + chunk_len] = chunk

        # write the mutated data back to the current input file
        with open(conf['current_input'], 'wb') as f_out:
            f_out.write(data)
