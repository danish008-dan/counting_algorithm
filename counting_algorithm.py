"""
File Purpose:
This program implements the Counting Sort algorithm.
Counting Sort is a non-comparison based sorting technique
used when the range of input values is known and small.
"""


def counting_sort(arr):
    # If the array is empty, return it directly
    if len(arr) == 0:
        return arr

    # Find the maximum value in the array
    max_element = max(arr)

    # Create a count array to store frequency of each element
    count = [0] * (max_element + 1)

    # Store the count of each element
    for num in arr:
        count[num] += 1

    # Modify count array to store cumulative counts
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Create an output array of the same size as input
    output = [0] * len(arr)

    # Build the output array using the count array
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1

    # Return the sorted array
    return output


# Example usage
if __name__ == "__main__":
    data = [4, 2, 2, 8, 3, 3, 1]

    print("Original Array:", data)
    sorted_data = counting_sort(data)
    print("Sorted Array:", sorted_data)
