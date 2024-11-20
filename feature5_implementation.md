In mutation.py, I changed the havoc_mutation function by adding
some features as the mutation strategy, such as:
1. Flipping a random bit in the seed
2. Selecting a short int, int, or long int (2, 4, or 8 bytes) from the seed file and adding or subtracting a random value3
3. Replacing a short int, int, or long int (2, 4, or 8 bytes) with specific "interesting" values, such as minimum, maximum, 0, -1, or 1
4. Replacing a random length chunk of bytes from the seed input with another chunk of bytes from the same file