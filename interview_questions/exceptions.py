numbers = [1, 2, 3, 4, 5, 6]

try:
    user_input = int(input(f"Enter a number between 0 to {len(numbers)-1}: "))
    print(numbers[user_input])
except ValueError:
    print("Invalid input! Please enter a valid integer.")
except IndexError:
    print(f"Wrong input...! Please enter a number between 0 to {len(numbers)-1}")
finally:
    print("Execution finished, whether an error occurred or not.")