# 1. Two Sum
# Problem:
# Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.
#
# Return the answer in any order.

# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]  (Because nums[0] + nums[1] == 9)

# ------------------------------------------------------------
# --- Brute Force Solution ---
# Idea:
# Check every possible pair (i, j).
# If nums[i] + nums[j] == target → return [i, j].
#
# Steps:
# 1. Loop i from 0 → n-1
# 2. Loop j from i+1 → n
# 3. If nums[i] + nums[j] == target → return [i, j]
#
# Time: O(n^2)  → nested loops
# Space: O(1)   → no extra data structures
# ------------------------------------------------------------

def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i]+nums[j] == target:
                return [i,j]

# Test
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]


# ------------------------------------------------------------
# --- Optimized Solution (HashMap) ---
# Idea:
# Use a HashMap (dictionary) to store numbers we’ve already seen.
# For each number, compute its complement = target - num.
# If the complement already exists in the map → return indices.
#
# Steps:
# 1. Create empty hashmap (seen = {})
# 2. Traverse list with index i:
#       complement = target - nums[i]
#       if complement in seen:
#           return [seen[complement], i]
#       else:
#           store this number → seen[nums[i]] = i
#
# Why this works:
# - You store each number and its index as you go.
# - For every new number, you just check if its pair is already seen.
#
# Time: O(n)  → each lookup in hashmap is O(1)
# Space: O(n) → for storing elements in hashmap
# ------------------------------------------------------------

def twoSum(nums, target):
    seen = {}  # hashmap to store num: index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement],i]
        else:
            seen[num]=i  # store number + index 
          

# Test
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]


# ------------------------------------------------------------
# --- Explanation of Key Line ---
# seen[num] = i
# means: store the number and its index
# Example dry run:
# nums = [2,7,11,15], target = 9
# Step 1: seen = {}, num=2, comp=7 → store {2:0}
# Step 2: num=7, comp=2 → found in seen → return [0,1]
# ------------------------------------------------------------
