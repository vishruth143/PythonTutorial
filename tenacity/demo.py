# Tenacity — Retrying in Python
# Tenacity is a general-purpose retrying library that simplifies adding retry logic to functions.
# It is useful when dealing with flaky operations such as network requests, database connections,
# or any code that may intermittently fail and succeed on a subsequent attempt.
#
# Key decorators and strategies:
#   - @retry                  : marks a function to be retried on failure
#   - stop_after_attempt(n)   : stops retrying after n total attempts
#   - wait_fixed(n)           : waits n seconds between each retry
#   - wait_exponential(...)   : increases wait time exponentially between retries
#   - retry_if_exception_type : only retry on specific exception types
#
# Flow:
#   1. Function is called → if it raises an exception, tenacity catches it
#   2. Waits the specified time, then calls the function again
#   3. Repeats until success or the stop condition is met
#   4. If all attempts fail → the last exception is re-raised

from tenacity import retry, stop_after_attempt, wait_fixed

# Define a function that may fail and needs retrying
@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def my_function():
    print("Trying function...")  # 👈 custom print to see retries

    # Code that may raise an exception or fail
    result = 1 / 0  # This will raise a ZeroDivisionError

    # If no exception is raised, return the result
    return result

try:
    # Call the function that may need retrying
    my_function()
except Exception as e:
    print("❌ Error occurred after retrying:", e)