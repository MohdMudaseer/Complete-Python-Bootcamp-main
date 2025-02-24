## PRocesses that run in parallel
### CPU-Bound Tasks-Tasks that are heavy on CPU usage (e.g., mathematical computations, data processing).
## PArallel execution- Multiple cores of the CPU

import multiprocessing
import time

def square():
    for i in range(5):
        time.sleep(1)
        print(f"square:{i*i}")
def cube():
    for i in range(5):
        time.sleep(1)
        print(f"cube;{i*i*i}")
if __name__=='__main__':
    p1=multiprocessing.Process(target=square)
    p2=multiprocessing.Process(target=cube)

    # start the process
    p1.start()
    p2.start()
    t=time.time()

    # wait for the processes to complete
    p1.join()
    p2.join()
    finished_time=time.time()-t
    print(f"finished_time:{finished_time}")
