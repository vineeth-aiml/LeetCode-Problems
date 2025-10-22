# ============================================================
# 11. Container With Most Water
# ============================================================

# 🧩 Problem:
# Given an integer array `height`, where each value represents
# the height of a vertical line drawn at that index.
#
# Find two lines that together with the x-axis form a container,
# such that the container can store the most water.
#
# Return the maximum area of water it can contain.
# ------------------------------------------------------------
# Example 1:
# Input:  height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation:
# The max area is formed between lines at index 1 (8) and index 8 (7):
# Width = 8 - 1 = 7
# Height = min(8, 7) = 7
# Area = 7 × 7 = 49
# ------------------------------------------------------------
# Constraints:
# 2 <= len(height) <= 10^5
# 0 <= height[i] <= 10^4
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# Check every pair (i, j) and calculate the area:
# area = (j - i) * min(height[i], height[j])
# Keep track of the maximum area.
#
# ⏱️ Time:  O(n²)
# 💾 Space: O(1)
# ------------------------------------------------------------

def maxArea_bruteforce(height):
    max_area = 0
    n = len(height)

    for i in range(n):
        for j in range(i + 1, n):
            width = j - i
            h = min(height[i], height[j])
            area = width * h
            max_area = max(max_area, area)
    return max_area


# Test Brute Force
print(maxArea_bruteforce([1,8,6,2,5,4,8,3,7]))  # ✅ 49



# ============================================================
# --- 2️⃣ Two Pointer Solution (Optimized) ---
# ============================================================
# 🧠 Idea:
# Use two pointers (left and right) starting at both ends.
# At each step:
#   - Compute area = (right - left) * min(height[left], height[right])
#   - Move the smaller height pointer inward.
#
# This ensures we always explore potentially higher heights
# while reducing width optimally.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1)
# ------------------------------------------------------------

def maxArea(height):
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        width = right - left
        h = min(height[left], height[right])
        area = width * h
        max_area = max(max_area, area)

        # Move the smaller height pointer
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area


# Test Two Pointer
print(maxArea([1,8,6,2,5,4,8,3,7]))  # ✅ 49



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach       | Time  | Space | Notes                       |
# |----------------|-------|--------|------------------------------|
# | Brute Force    | O(n²) | O(1)  | Checks all pairs             |
# | Two Pointers   | O(n)  | O(1)  | ✅ Best and most efficient    |
# ============================================================
