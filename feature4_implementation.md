In schedule.py, I modified the get_power_schedule function to
implement a simplified AFL's scoring implementation. I only calculated
2 scoring methods, execution time score and coverage score by comparing them with their
respective averages. Then, I summed those 2 scores and divide them by 100.

To keep track of the averages, I added total_exec_time and total_coverage variables in main.py. 
In every loop, I incremented those two variables. Moreover, I added a function called calculate_avg 
in schedule.py to calculate the averages