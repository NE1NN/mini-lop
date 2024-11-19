In seed.py, I added a new field priority to help me track the priority and 
used_in_cycle to track if the seed has been used in the cycle. In main.py, I also
keep a cycle tracker to track the cycle.

I modified select_next_seed function in schedule.py. I followed AFL's 
favor implementation by the execution times * the size of the file.
The lower it is, the higher the priority is in the queue. Then,
I mark the one with the highest priority (lowest execution times * file size)
as favoured. Then, I have 2 arrays, one for the favoured seeds and another for the unfavoured ones.
Also, I set such that there is 20% chance of returning non favoured seeds and 80% of returning favoured seeds.
This is to avoid starving some potentially good seeds.

