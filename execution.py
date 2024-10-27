import os
import time
from feedback import clear_shm


def run_target(ctl_write_fd, st_read_fd, trace_bits):
    # need to clear the shared memory before running the target
    clear_shm(trace_bits)

    start_time = time.time()
    # lscpu | grep "Byte Order"
    os.write(ctl_write_fd, (0).to_bytes(4, byteorder='little'))

    # print only for debugging purpose
    grandchild_pid_bytes = os.read(st_read_fd, 4)
    # print("grandchild pid is {}".format(int.from_bytes(grandchild_pid_bytes, byteorder='little', signed=False)))

    status_bytes = os.read(st_read_fd, 4)
    status_code = int.from_bytes(status_bytes, byteorder='little', signed=False)
    end_time = time.time()
    exec_time = end_time - start_time
    # print(f"status is {status_code}")
    # print(f"Execution time: {exec_time} seconds")

    return status_code, exec_time
