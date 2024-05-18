def recursiveHanoi(n, s, a, d):
    if n == 1:
        print(s + " to " + d)
        return 1  # Increment the move count for the base case

    # Move n-1 disks from source to auxiliary
    moves = recursiveHanoi(n-1, s, d, a)
    print(s + " to " + d)  # Move the nth disk from source to destination
    moves += 1  # Increment the move count for this step
    # Move the n-1 disks from auxiliary to destination
    moves += recursiveHanoi(n-1, a, s, d)
    return moves  # Return the total moves made for this step and all recursive steps

# Example usage:
n = 3
source = '1'
auxiliary = '2'
destination = '3'
total_moves = recursiveHanoi(n, source, auxiliary, destination)

print(f"Total moves taken: {total_moves}")

     