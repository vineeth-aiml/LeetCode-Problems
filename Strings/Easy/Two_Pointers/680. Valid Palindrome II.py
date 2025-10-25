# ============================================================
# 680. Valid Palindrome II
# ============================================================

# ## Problem
# Given a string `s`, return True if it can become a palindrome
# after deleting at most one character.
#
# ### Examples
# - "aba" → True  
# - "abca" → True  (remove 'c' → "aba")  
# - "abc" → False  
#
# ---
# ## Brute Force Approach
# 1. Check if `s` is already a palindrome → return True.
# 2. For every index `i`, remove one character: `s[:i] + s[i+1:]`.
# 3. If any of those new strings is a palindrome → return True.
# 4. Otherwise → return False.
#
# ⏱️ Time: O(n²)  
# 💾 Space: O(n)  (due to slicing)
# ------------------------------------------------------------

def validPalindrome_bruteforce(s):
    def is_palindrome(x):
        return x == x[::-1]

    if is_palindrome(s):
        return True

    # Try removing each character once
    for i in range(len(s)):
        temp = s[:i] + s[i+1:]
        if is_palindrome(temp):
            return True
    return False


# Test Brute Force
print(validPalindrome_bruteforce("abca"))  # ✅ True
print(validPalindrome_bruteforce("abc"))   # ❌ False
print(validPalindrome_bruteforce("aba"))   # ✅ True

# ------------------------------------------------------------
# ## Optimal (Two Pointers + Greedy)
# 1. Use two pointers: `l` (left) and `r` (right).
# 2. Compare s[l] and s[r]:
#    - If equal → move both inward.
#    - If not equal → try skipping either s[l] or s[r].
# 3. If any one skip leads to palindrome → return True.
#
# ✅ Greedy because we delete at most one mismatched char.
# ⏱️ Time: O(n)
# 💾 Space: O(1)
# ------------------------------------------------------------

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(l, r):
            """Check if substring s[l:r+1] is palindrome"""
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                # Try deleting either side once
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l += 1
            r -= 1

        return True


# Test Optimal
sol = Solution()
print(sol.validPalindrome("abca"))  # ✅ True
print(sol.validPalindrome("abc"))   # ❌ False
print(sol.validPalindrome("deeee")) # ✅ True
print(sol.validPalindrome("abccdba")) # ✅ True

# ============================================================
# 🧾 Summary
# ============================================================
# | Approach        | Time  | Space | Notes |
# |-----------------|-------|--------|--------|
# | Brute Force     | O(n²) | O(n)  | Tries removing each char |
# | Two Pointers ✅  | O(n)  | O(1)  | Best + Greedy + Efficient |
# ============================================================
