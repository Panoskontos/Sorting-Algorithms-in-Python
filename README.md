# Sorting-Algorithms-in-Python

<br>

This is a project that tests 4 basic sorting algorithms in python on RANDOM arrays of sizes 10, 100, 1000, 10000, 100000

<br>

| Big-O     | Bubble Sort | Insertion Sort     | Quick Sort  | Merge Sort     |
| :---        |    :----:   |          ---: |  ---: |  ---: |
| Time Complexity     | O(n^2)       | O(n^2)   |    O(nlogn)   | O(nlogn)   |
| Space Complexity   | O(1)       | O(1)        |     O(logn)      | O(n)
| Stability   | Stable       | Stable         |     Non-stable     | Stable

<br>
<br>

## These are my results:

![algorithm_second_tests](https://user-images.githubusercontent.com/65974766/144761486-0187a7a6-80cd-4b34-8b23-5ab93b2d76d0.jpg)


Wow quick sort algorithm sorted an array of 100.000 numbers is less that 0.7 seconds
<br>
It is evident that Quick Sort is the supreme one in terms of speed
- 5.873 times faster than Bubble Sort
- 3.627 times faster than Insertion Sort
- almost 2.5 times faster than Merge Sort
<br>
However we should always take into account it's space complexity and lack of stability
