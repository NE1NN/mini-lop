In schedule.py, I modified the get_power_schedule function to
implement a simplified AFL's scoring implementation. I only calculated
2 scoring methods, execution time score and coverage score by comparing them with their
respective averages. Then, I have a variable called HAVOC_MAX_MULT as an upperbound. Currently, it's set to 16, which is similar to AFL.
If the score is bigger than HAVOC_MAX_MULT * 100, I set the score as HAVOC_MAX_MULT * 100

To keep track of the averages, I added total_exec_time and total_coverage variables in main.py. 
In every loop, I incremented those two variables. Moreover, I added a function called calculate_avg 
in schedule.py to calculate the averages