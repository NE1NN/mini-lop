I modified select_next_seed function in schedule.py. I followed AFL's 
favor implementation by the execution times * the size of the file.
The lower it is, the higher the priority is in the queue. Then,
I mark the one with the highest priority (lowest execution times * file size)
as favoured. Then, I have 2 arrays, one for the favoured seeds and another for the unfavoured ones.
Also, I set such that there is 20% chance of returning non favoured seeds and 80% of returning favoured seeds.
This is to avoid starving some potentially good seeds.

I then find all the seeds that haven't been used in the cycle.
