#| Implement a job scheduler which takes in a function f and an integer n,
#| and calls f after n milliseconds.

import threading
import time

def job_scheduler(f, n):
    #| Define a nested function that will be executed after the delay
    def delayed_execution():
        #| Sleep for the specified duration (convert milliseconds to seconds)
        time.sleep(n / 1000.0)
        #| Call the provided function f after the sleep
        f()

    #| Create a new thread with the delayed_execution function as the target
    thread = threading.Thread(target=delayed_execution)
    #| Start the thread to begin the countdown and execution
    thread.start()

#| Example usage:
def example_function():
    print("Function executed!")

#| Schedule 'example_function' to be called after 2000 milliseconds (2 seconds)
job_scheduler(example_function, 2000)
