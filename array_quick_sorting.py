def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def replace_elements(arr, target, replacement):
    for i in range(len(arr)):
        if arr[i] == target:
            arr[i] = replacement

def main():
    try:
        input_str = input("Enter an array of integers (comma-separated): ")
        input_list = [int(x) for x in input_str.split(",")]

        quick_sort(input_list, 0, len(input_list) - 1)

        target = int(input("Enter the target element to search for: "))
        if target in input_list:
            replacement = int(input("Enter the replacement element: "))
            replace_elements(input_list, target, replacement)
        else:
            print(f"Target element {target} not found in the array.")

        print("Modified array:")
        print(input_list)

    except ValueError:
        print("Invalid input. Please enter a valid comma-separated list of integers.")

main()  # Call the main function directly
