In mutation.py, I added two new functions, havoc_mutation_operation and 
save_to_input. These functions were extracted to reduce coupling and improve modularity as they will be used again in feature 6.

The havoc_mutation_operation implements some mutation strategies, such as:
1. Selecting a short int, int, or long int (2, 4, or 8 bytes) from the seed file and adding or subtracting a random value
2. Replacing a short int, int, or long int (2, 4, or 8 bytes) with specific "interesting" values, such as minimum, maximum, 0, -1, or 1
3. Replacing a random length chunk of bytes from the seed input with another chunk of bytes from the same file

Each seed will go through those 3 stages to ensure it's randomized properly

The save_to_input function is responsible for saving the mutated data to the current_input file