# ============================================================
# 942. DI String Match
# ============================================================

# 🧩 Problem:
# Given a string s of length n, consisting of 'I' (increase) and 'D' (decrease),
# reconstruct a permutation of numbers [0,1,...,n] such that:
# - s[i] == 'I' → perm[i] < perm[i+1]
# - s[i] == 'D' → perm[i] > perm[i+1]
# Return any valid permutation.

# ------------------------------------------------------------
# Example 1:
# Input:  s = "IDID"
# Output: [0,4,1,3,2]
#
# Example 2:
# Input:  s = "III"
# Output: [0,1,2,3]
#
# Example 3:
# Input:  s = "DDI"
# Output: [3,2,0,1]
# ------------------------------------------------------------
#
# Constraints:
# 1 <= s.length <= 10^5
# s[i] is either 'I' or 'D'
# ------------------------------------------------------------
# 🧠 Edge Cases:
# - All 'I': "III" → [0,1,2,3,...]
# - All 'D': "DDD" → [n,n-1,...,0]
# - Mixed: "IDID" → [0,4,1,3,2] or any valid permutation
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Generate all permutations of [0..n].
# 2. Check each permutation against the string s:
#    - 'I' → current < next
#    - 'D' → current > next
# 3. Return the first valid permutation.
#
# ⚠ Only usable for very small n due to factorial time.
#
# ⏱️ Time:  O((n+1)! * n)
# 💾 Space: O(n)
# ------------------------------------------------------------

from itertools import permutations

def diStringMatch(s):
    n = len(s)
    nums = list(range(n + 1))
    
    for perm in permutations(nums):
        valid = True
        for i, ch in enumerate(s):
            if ch == 'I' and perm[i] >= perm[i+1]:
                valid = False
                break
            if ch == 'D' and perm[i] <= perm[i+1]:
                valid = False
                break
        if valid:
            return list(perm)
    return []

# ✅ Test Brute Force
print(diStringMatch("IDID"))  # [0,4,1,3,2] (or another valid)


# ============================================================
# --- 2️⃣ Two Pointers Solution (Optimized) ---
# ============================================================
# 🧠 Idea:
# - Use two pointers low=0, high=n.
# - For each char in s:
#   - 'I' → append low, increment low
#   - 'D' → append high, decrement high
# - Append last remaining number.
#
# ✅ Works in O(n) time and O(n) space
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def diStringMatch(s):
    low, high = 0, len(s)
    perm = []

    for ch in s:
        if ch == 'I':
            perm.append(low)
            low += 1
        else:  # 'D'
            perm.append(high)
            high -= 1

    perm.append(low)  # last remaining number
    return perm

# ✅ Test Optimized
print(diStringMatch("IDID"))  # [0,4,1,3,2]
print(diStringMatch("III"))   # [0,1,2,3]
print(diStringMatch("DDI"))   # [3,2,0,1]


# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach         | Time                 | Space | Notes                                |
# |------------------|--------------------|-------|-------------------------------------|
# | Brute Force      | O((n+1)! * n)      | O(n)  | ✅ Simple, only for small n          |
# | Two Pointers     | O(n)               | O(n)  | ✅ Optimal, fast, works for large n  |
# ============================================================
