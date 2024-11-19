In seed.py, I added a new field priority to track the priority of each seed, and 
used_in_cycle to track if the seed has been used in the current cycle. In main.py, I added
a cycle tracker to track of the cycle.

In schedule.py, I modified select_next_seed function. I followed AFL's 
favor implementation by multiplying the execution time and the file size.
The lower it is, the higher the priority is in the queue. Then,
I mark the one with the highest priority (lowest execution times * file size)
as favoured. 

To ensure that at least every seed is used, I used the used_in_cycle 
to find all unused seeds. Moreover, I created 2 arrays, one for the 
favoured seeds and another for the non favoured ones.  When selecting a seed, 
there is an 80% chance of choosing from the favored seeds and a 20% chance of selecting 
from the unfavored seed. This is to avoid starving some potentially good seeds.

