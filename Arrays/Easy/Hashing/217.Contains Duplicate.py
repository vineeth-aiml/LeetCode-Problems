# ============================================================
# 217. Contains Duplicate
# ============================================================

# 🧩 Problem:
# Given an integer array nums, return True if any value 
# appears at least twice in the array, and return False 
# if every element is distinct.
#
# Example:
# Input:  nums = [1,2,3,1]
# Output: True  (because 1 appears twice)
#
# Input:  nums = [1,2,3,4]
# Output: False (all elements unique)
#
# ------------------------------------------------------------
# Constraints:
# 1 <= len(nums) <= 10^5
# -10^9 <= nums[i] <= 10^9
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# Compare every element with every other element.
# If any pair is equal → duplicate found.
#
# Steps:
# 1. Loop i from 0 → n-1
# 2. Loop j from i+1 → n
# 3. If nums[i] == nums[j] → return True
# 4. If loop ends → return False
#
# ⏱️ Time:  O(n²)
# 💾 Space: O(1)
# ------------------------------------------------------------

def containsDuplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                return True
    return False

# Test
nums = [1, 2, 3, 1]
print(containsDuplicate(nums))  # ✅ True (duplicate found)



# ============================================================
# --- 2️⃣ Sorting-Based Solution ---
# ============================================================
# 🧠 Idea:
# Sort the array first. Then check if any adjacent elements are equal.
#
# Steps:
# 1. Sort nums → all duplicates will come together.
# 2. Loop from index 1 → n-1
# 3. If nums[i] == nums[i-1] → duplicate found
# 4. Else return False
#
# ⏱️ Time:  O(n log n)   (because of sorting)
# 💾 Space: O(1)          (in-place sort)
# ------------------------------------------------------------

def containsDuplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(1, n):
        if nums[i] == nums[i-1]:
            return True
    return False

# Test
nums = [1, 2, 3, 4, 1]
print(containsDuplicate(nums))  # ✅ True



# ============================================================
# --- 3️⃣ HashSet-Based Solution (Most Optimal) ---
# ============================================================
# 🧠 Idea:
# Use a set to track seen elements.
# If an element already exists in the set → duplicate found.
#
# Steps:
# 1. Create empty set "seen".
# 2. Loop through each num in nums.
# 3. If num in seen → return True.
# 4. Else add num to seen.
# 5. Return False if loop finishes.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Test
nums = [1, 2, 3, 4]
print(containsDuplicate(nums))  # ✅ False (no duplicates)



# ============================================================
# --- 4️⃣ HashMap-Based Solution (Alternative) ---
# ============================================================
# 🧠 Idea:
# Similar to set, but store elements as keys in a dictionary.
# If element already exists → duplicate found.
#
# Steps:
# 1. Create empty dict "count".
# 2. Traverse array.
# 3. If num already in count → return True.
# 4. Else add num: True.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def containsDuplicate(nums):
    count = {}
    for num in nums:
        if num in count:
            return True
        count[num] = True
    return False

# Test
nums = [10, 20, 30, 10]
print(containsDuplicate(nums))  # ✅ True (duplicate found)



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach       | Time      | Space | Notes |
# |----------------|-----------|--------|--------|
# | Brute Force    | O(n²)     | O(1)   | Slow, only for small arrays |
# | Sorting        | O(n log n)| O(1)   | Faster, but changes order |
# | HashSet        | O(n)      | O(n)   | ✅ Best performance |
# | HashMap        | O(n)      | O(n)   | Same as set, more flexible |
# ============================================================

