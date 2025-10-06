
# 26. Remove Duplicates from Sorted Array

# Problem:
# Given a sorted integer array nums, remove duplicates in-place such that each unique element appears only once.
# Return the number of unique elements k and make sure the first k elements of nums contain the unique elements in order.
# The elements beyond k don’t matter.


# --- Brute Force ---

# Steps:

# Create an empty list unique.

# Traverse nums.

# If element is not in unique, append it.

# Copy elements from unique back into nums.

# Return the length of unique.
# Time: O(n²), Space: O(n)


def removeDuplicates(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    for i in range(len(unique)):
        nums[i] = unique[i]
    return len(unique)

# Example
nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k, nums)  # Output: 5 [0,1,2,3,4,2,2,3,3,4]



#  Two-Pointer Steps (Compact + Inline Explanation)

# slow = 0 → last unique element index (first element is always unique).

# For fast = 1 → len(nums)-1 → scan the array for new elements:

#     If nums[fast] != nums[slow] → found a new unique element:

#         slow += 1 → move slow pointer to next position.

#         nums[slow] = nums[fast] → place the unique element in order.

# Return slow + 1 → total count of unique elements (k).


def removeDuplicates(nums):

    slow = 0

    for fast in range(1,len(nums)):
        if nums[slow] != nums[fast]:
            slow+=1
        nums[slow]=nums[fast]
    
    return slow+1

# Example
nums = [0,0,1,1,1,2,2,3,3,4]
k = removeDuplicates(nums)
print(k, nums)  # Output: 5 [0,1,2,3,4,2,2,3,3,4]