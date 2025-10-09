# ============================================================
# 167. Two Sum II - Input Array Is Sorted
# ============================================================

# 🧩 Problem:
# Given a 1-indexed array of integers numbers that is already sorted 
# in non-decreasing order, find two numbers such that they add up 
# to a specific target number.
#
# Let these two numbers be numbers[index1] and numbers[index2], 
# where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers as [index1, index2].
#
# Each input has exactly one valid answer, and the same element 
# cannot be used twice.
#
# ⚠️ Must use only constant extra space.
#
# ------------------------------------------------------------
# Example 1:
# Input:  numbers = [2,7,11,15], target = 9
# Output: [1,2]  (Because 2 + 7 = 9)
#
# Example 2:
# Input:  numbers = [2,3,4], target = 6
# Output: [1,3]
#
# Example 3:
# Input:  numbers = [-1,0], target = -1
# Output: [1,2]
# ------------------------------------------------------------

# Constraints:
# 2 <= numbers.length <= 3 * 10^4
# -1000 <= numbers[i] <= 1000
# -1000 <= target <= 1000
# numbers is sorted in non-decreasing order.
# Exactly one solution exists.
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# Try all possible pairs (i, j) and check if their sum equals target.
#
# Steps:
# 1. Loop i from 0 → n-1
# 2. Loop j from i+1 → n
# 3. If numbers[i] + numbers[j] == target → return [i+1, j+1]
#
# ⏱️ Time:  O(n²)
# 💾 Space: O(1)
# ------------------------------------------------------------

def twoSum(numbers, target):
    n = len(numbers)
    for i in range(n):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == target:
                return [i + 1, j + 1]

# Test
numbers = [2, 7, 11, 15]
target = 9
print(twoSum(numbers, target))  # ✅ [1, 2]


# ============================================================
# --- 2️⃣ HashMap-Based Solution ---
# ============================================================
# 🧠 Idea:
# Store previously seen numbers in a hashmap {num: index}.
# For each number, check if its complement (target - num) is already seen.
#
# Steps:
# 1. Create empty dict `seen = {}`.
# 2. Traverse each num with index i.
# 3. Calculate complement = target - num.
# 4. If complement in seen → return [seen[complement], i+1].
# 5. Else store current num with its 1-based index → seen[num] = i+1.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ⚠️ Not constant space, but easy to understand.
# ------------------------------------------------------------

def twoSum(numbers, target):
    seen = {}
    for i, num in enumerate(numbers):
        complement = target - num
        if complement in seen:
            return [seen[complement], i + 1]
        seen[num] = i + 1

# Test
numbers = [2, 3, 4]
target = 6
print(twoSum(numbers, target))  # ✅ [1, 3]


# ============================================================
# --- 3️⃣ Two-Pointer Solution (Optimal) ---
# ============================================================
# 🧠 Idea:
# Since the array is sorted, use two pointers:
#   left → start (0)
#   right → end (n-1)
# Move pointers inward based on sum comparison.
#
# Steps:
# 1. Initialize left = 0, right = n-1.
# 2. While left < right:
#       sum = numbers[left] + numbers[right]
#       if sum == target → return [left+1, right+1]
#       if sum < target  → move left += 1 (need bigger sum)
#       else             → move right -= 1 (need smaller sum)
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1) ✅ Constant space (Best)
# ------------------------------------------------------------

def twoSum(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1

# Test
numbers = [-1, 0]
target = -1
print(twoSum(numbers, target))  # ✅ [1, 2]


# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach         | Time      | Space | Works for Sorted? | Notes                  |
# |------------------|-----------|--------|------------------|------------------------|
# | Brute Force      | O(n²)     | O(1)   | ✅                | Simple but slow        |
# | HashMap          | O(n)      | O(n)   | ✅                | Easy logic, not const. |
# | Two Pointers ✅   | O(n)      | O(1)   | ✅✅✅             | 🚀 Best choice          |
# ============================================================
