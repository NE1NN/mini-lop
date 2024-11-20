I added a function called splice_mutation in mutation.py, which implements a splice mutator. It works like this:
1. Select a seed and another seed from the queue (ensuring they are not the same)
2. For each of the two seeds, randomly split them into two halves
3. Combine the first half of the first seed with the second half of the second seed to generate a new test input
4. Apply the havoc_mutation function to the newly generated test input to introduce additional randomness
5. Yield the mutated test input for execution

Since the havoc_mutator was already implemented in feature 5, I just called that function at the end of splice_mutation function.

Now that I have 2 mutators, I updated main.py to randomly select between them with a 50% chance for each