# ============================================================
# 27. Remove Element
# ============================================================

# 🧩 Problem:
# Given an integer array `nums` and an integer `val`, remove **all occurrences**
# of `val` in-place. The order of elements may change.
#
# Then, return the number of elements in `nums` that are **not equal** to `val`.
#
# After removal:
# - The first `k` elements of `nums` should contain the remaining valid numbers.
# - The remaining elements beyond `k` are not important (can be ignored).
#
# ------------------------------------------------------------
# Example 1:
# Input:  nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: 
# After removing 3s, only [2,2] remain. k = 2.
#
# Example 2:
# Input:  nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation:
# The first five elements are [0,1,4,0,3]. k = 5.
# Remaining positions are ignored.
# ------------------------------------------------------------
#
# Constraints:
# 0 <= len(nums) <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# Use a temporary list to collect all elements that are NOT equal to val.
# Then copy them back into nums.
#
# Steps:
# 1. Initialize an empty list `temp`.
# 2. Traverse all elements of nums.
# 3. If nums[i] != val → append to temp.
# 4. Copy all elements of temp back into nums (in-place update).
# 5. Return len(temp) as k.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def removeElement(nums, val):
    temp = []

    # Step 1: Collect elements that are not val
    for n in nums:
        if n != val:
            temp.append(n)

    # Step 2: Copy back to nums
    for i in range(len(temp)):
        nums[i] = temp[i]

    # Step 3: Return count of valid elements
    return len(temp)


# Test
nums = [3, 2, 2, 3]
val = 3
k = removeElement(nums, val)
print(k, nums)  # ✅ 2 [2, 2, 2, 3] (first two valid elements are [2,2])



# ============================================================
# --- 2️⃣ Two Pointers Solution (Optimized) ---
# ============================================================
# 🧠 Idea:
# Use **two pointers** to perform in-place replacement:
# - `l` → Scans each element.
# - `r` → Tracks the position to place the next valid element.
#
# Steps:
# 1. Initialize l = 0, r = 0
# 2. Traverse the array:
#       - If nums[l] != val → copy nums[l] to nums[r] and increment r
#       - Always move l forward
# 3. After loop ends, r = count of valid elements.
# 4. Return r.
#
# ✅ In-place modification (no extra space).
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1)
# ------------------------------------------------------------

def removeElement(nums, val):
    l, r = 0, 0

    while l < len(nums):
        if nums[l] != val:
            nums[r] = nums[l]
            r += 1
        l += 1

    return r


# Test
nums = [0,1,2,2,3,0,4,2]
val = 2
k = removeElement(nums, val)
print(k, nums)  # ✅ 5 [0,1,3,0,4,0,4,2] → first 5 valid are [0,1,3,0,4]



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach       | Time | Space | Notes |
# |----------------|------|--------|--------|
# | Brute Force    | O(n) | O(n)  | Creates new list |
# | Two Pointers   | O(n) | O(1)  | ✅ Best & in-place |
# ============================================================
