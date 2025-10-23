# ============================================================
# 75. Sort Colors
# ============================================================

# 🧩 Problem:
# Given an array `nums` containing n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with colors in the order red (0), white (1), and blue (2).
#
# You must solve this problem **without using the built-in sort()**
# and **using only constant extra space**.
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Example 2:
# Input:  nums = [2,0,1]
# Output: [0,1,2]
# ------------------------------------------------------------
# Constraints:
# 1 <= len(nums) <= 300
# nums[i] ∈ {0, 1, 2}
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution (Counting Sort Idea) ---
# ============================================================
# 🧠 Idea:
# Count how many 0s, 1s, and 2s appear in the array.
# Then, overwrite the array in that order:
#   - First count0 elements → 0
#   - Next count1 elements → 1
#   - Remaining count2 elements → 2
#
# ⏱️ Time:  O(2n) ≈ O(n)
# 💾 Space: O(1)
# ------------------------------------------------------------

def sortColors_bruteforce(nums):
    count0 = count1 = count2 = 0

    # Step 1: Count occurrences
    for x in nums:
        if x == 0:
            count0 += 1
        elif x == 1:
            count1 += 1
        else:
            count2 += 1

    # Step 2: Overwrite array
    i = 0
    for _ in range(count0):
        nums[i] = 0
        i += 1
    for _ in range(count1):
        nums[i] = 1
        i += 1
    for _ in range(count2):
        nums[i] = 2
        i += 1


# ✅ Test Brute Force
nums = [2,0,2,1,1,0]
sortColors_bruteforce(nums)
print(nums)  # [0,0,1,1,2,2]



# ============================================================
# --- 2️⃣ Optimal Solution (Dutch National Flag Algorithm) ---
# ============================================================
# 🧠 Idea:
# Use three pointers → low, mid, high:
#   - [0...low-1] → all 0s
#   - [low...mid-1] → all 1s
#   - [high+1...end] → all 2s
#
# Traverse with mid:
#   - If nums[mid] == 0 → swap(nums[low], nums[mid]); low++, mid++
#   - If nums[mid] == 1 → mid++
#   - If nums[mid] == 2 → swap(nums[mid], nums[high]); high--
#
# ✅ Single pass, in-place, constant space.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1)
# ------------------------------------------------------------

def sortColors(nums):
    low, mid, high = 0, 0, len(nums) - 1

    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:  # nums[mid] == 2
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1


# ✅ Test Optimal
nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)  # [0,0,1,1,2,2]



# ================================================================================
# 🧾 Summary Comparison                                                          |
# ================================================================================
# | Approach                | Time  | Space | Passes | Notes                      |
# |--------------------------|-------|--------|--------|--------------------------|
# | Brute Force (Counting)   | O(n)  | O(1)  | 2      | Simple & clear            |
# | Dutch National Flag Algo | O(n)  | O(1)  | ✅ 1    | Best & most efficient 🚀|
# ================================================================================
