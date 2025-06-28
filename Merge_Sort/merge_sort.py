from pygments.lexers.whiley import WhileyLexer


#Split the number input into two list and send to merge function
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    first = merge_sort(nums[:len(nums)//2])
    second = merge_sort(nums[len(nums)//2:])
    return merge(first, second)

def merge(first, second):
    final = []
    i, j  = 0, 0

    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1

    ## Handle last number in odd numbered lists
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1

    return final

def main():
    print("## Merge Sort ##")
    print("List of numbers:")
    nums = [5, 20, 100, 23, 55, 32, 14, 10, 16, 21, 81, 86, 44]
    print(f"List of nums", nums)
    print("Sorted List:")
    print(merge_sort(nums))

if __name__=="__main__":
    main()
