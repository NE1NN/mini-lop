I modified feedback.py and main.py. In feedback.py, I modified the check_coverage function
by looping through the bitmap and find the bits that is not 0, indicating a visited path.
If the visited path is not currently listed in the global_coverage, then a new path has been found. The path will be added to global_coverage and global_coverage will be returned as True

In main.py, if the return value of new_edge_covered value from check_coverage is True, then 
the path to the seed is saved to the queue folder and is appended to seed_queue