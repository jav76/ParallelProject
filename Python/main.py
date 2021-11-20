import math
import multiprocessing
import time
from mpmath import *

thread_count = 8
iterations = 1000

# Sets the precision to 15 decimal places because we are using doubles for our C implementation.
mp.dps = 15

def euler_approximation(n, rank, return_val):
    local_chunk = math.floor(n / thread_count)
    local_sum = 0

    for i in range(1, local_chunk + 1):
        """
        This 'chunked_n' value splits the factorials up between processes so that the last process
        doesn't take much longer with larger numbers.
        Ex: 
        chunked_n with 4 threads 20 iterations:
            1, 5, 9, 13, 17
            2, 6, 10, 14, 18
            3, 7, 11, 15, 19
            0, 4, 8, 12, 16
        instead of something like:
            0, 1, 2, 3, 4
            5, 6, 7, 8, 9
            10, 11, 12, 13, 14
            15, 16, 17, 18, 19
        """
        chunked_n = thread_count * (i - 1) + rank
        #print(chunked_n)
        factorial = mpf(math.factorial(chunked_n))
        local_sum = mpf(local_sum + factorial ** -1)
    #print(local_sum)
    return_val[rank] = mpf(local_sum)


if __name__ == '__main__':
    threads = []
    manager = multiprocessing.Manager()
    return_val = manager.dict()
    start_time = time.time()

    for i in range(0, thread_count):
        new_thread = multiprocessing.Process(target=euler_approximation, args=(iterations, i, return_val))
        threads.append(new_thread)
        new_thread.start()
    for i in threads:
        i.join()

    end_time = time.time()
    run_time = end_time - start_time
    sum = 0
    # Serial sum each thread's part
    for i in range(0, thread_count):
        sum += return_val[i]

    print(f"Estimated e:        {sum}")
    print(f"Runtime (seconds):  {run_time}")
