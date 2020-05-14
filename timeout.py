"""
Description:
time.time() = number of seconds since 1st January 1970

While loop will run for "timeout" seconds
"""
import time

initial_time = time.time()
timeout = 45


while time.time()-initial_time < timeout:
    # Insert Code Here