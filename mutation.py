import random


def havoc_mutation(conf, seed):
    # this is a dummy implementation, it just randomly flips some bytes
    # TODO: implement the havoc mutation similar to AFL
    with open(seed.path, 'rb') as f:
        data = bytearray(f.read())

        data_len = len(data)

        for _ in range(random.randint(1, data_len)):
            # Randomly select a byte index to flip
            byte_index = random.randint(0, data_len - 1)

            # Randomly select a bit to flip within the byte
            bit_position = random.randint(0, 7)

            # Flip the selected bit in the byte using XOR
            data[byte_index] ^= (1 << bit_position)

        # write the mutated data back to the current input file
        with open(conf['current_input'], 'wb') as f_out:
            f_out.write(data)
