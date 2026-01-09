def custom_reverse(input_str):
    # Step 1: reverse the entire string
    reversed_str = input_str[::-1].replace(" ", "")  # remove spaces

    # Step 2: split into original word lengths
    word_lengths = [len(word) for word in input_str.split()]

    result = []
    index = 0
    for length in word_lengths:
        result.append(reversed_str[index:index + length])
        index += length

    return " ".join(result)


# Example usage
input_str = "write test cases in java"
print(custom_reverse(input_str))  # Output: "avajn ises actse te tirw"
