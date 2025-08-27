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