## Overview

Counting Sort is a non-comparison based sorting algorithm that sorts elements by counting the frequency of each distinct value. It is most efficient when the range of input values is small and known in advance.

Unlike comparison-based algorithms such as Quick Sort or Merge Sort, Counting Sort achieves linear time complexity under suitable conditions.

## Algorithm Explanation

Find the maximum element in the input array.

Create a count array to store the frequency of each element.

Modify the count array to store cumulative counts.

Place elements into the correct position in the output array.

Return the sorted array.

## Time and Space Complexity
Case	Complexity
Best Case	O(n + k)
Average Case	O(n + k)
Worst Case	O(n + k)
Space Complexity	O(k)

Where:

n is the number of elements

k is the range of input values

## Project Structure
counting_sort.py
README.md

## How to Run

Ensure Python is installed on your system.

Open a terminal in the project directory.

Run the following command:

python counting_sort.py

## Features

Non-comparison based sorting algorithm

Stable sorting technique

Efficient for small-range integer data

Simple and easy-to-understand implementation

## Limitations

Works only with non-negative integers

Not suitable for large ranges of input values

Requires additional memory for the count array

## Applications

Sorting integers with a limited range

Used as a subroutine in Radix Sort

Frequency-based data processing

Competitive programming problems

## Conclusion

Counting Sort is an efficient and stable sorting algorithm for datasets where the value range is limited. It provides linear time performance and serves as a foundation for advanced sorting techniques like Radix Sort.
