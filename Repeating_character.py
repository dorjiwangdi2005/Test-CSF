def find_first_repeating_character(s):
    char_count = {}  # Dictionary to store character counts

    for char in s:
        if char in char_count:
            # Character repeated, print it and its memory address
            print(f"First repeating character: '{char}'")
            print(f"Memory address: {id(char)}")
            return char
        else:
            char_count[char] = 1

    # No repeating character found
    print("No repeating character in the string.")
    return None

# Example usage:
input_string = "hello"
result = find_first_repeating_character(input_string)
if result:
    print(f"Character '{result}' repeated at memory address {id(result)}")
else:
    print("No repeating character found.")
