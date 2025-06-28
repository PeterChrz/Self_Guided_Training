"""
merge_sort.py - Minimal merge sort algorithm

When executed directly it will print
and sort a list of numbers.

    $ python merge_sort.py
"""

def merge_sort(nums):
    """
    Recursively split nums until each group has <= 1 element.
    Rebuild the list in an ascending sorted order.

    Time Complexity: 0(n log n)
    Space Complexity: 0(n)
    """

    if len(nums) < 2:
        return nums

    first = merge_sort(nums[:len(nums)//2])
    second = merge_sort(nums[len(nums)//2:])
    return merge(first, second)

def merge(first, second):
    """
    Takes two sorted lists into a single sorted list.
    The function walks through both inputs in linear time,
    choosing the smaller element at each step.
    """

    final = []
    i, j  = 0, 0

    # Walk until we exhaust the elements in each list.
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    ## Handle any leftover numbers in odd numbered lists
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1

    return final

def main():
    # Example Implementation.
    print("## Merge Sort ##")

    nums = [5, 20, 100, 23, 55, 32, 14, 10, 16, 21, 81, 86, 44]
    print("List of numbers:")
    print(f"{nums}")

    print("Sorted List:")
    print(merge_sort(nums))

# Entry-point guard runs only when executed, not when imported.
if __name__=="__main__":
    main()
