# ============================================================
# 5. Longest Palindromic Substring
# ============================================================

# ## Problem
# Given a string `s`, return the longest substring that is a palindrome.
#
# ### Examples
# - "babad" → "bab" or "aba"  
# - "cbbd" → "bb"  
# - "a" → "a"  
# - "" → ""  
#
# ------------------------------------------------------------
# ## Brute Force Approach
# 1. Check all substrings s[i:j+1].  
# 2. If substring is a palindrome and longer than current longest → update.  
#
# ⏱️ Time: O(n³)  
# 💾 Space: O(1)  
# ------------------------------------------------------------

def longestPalindrome_bruteforce(s):
    n = len(s)
    longest = ""
    for i in range(n):
        for j in range(i+1, n+1):
            sub = s[i:j]
            if sub == sub[::-1] and len(sub) > len(longest):
                longest = sub
    return longest

# Test Brute Force
print(longestPalindrome_bruteforce("babad"))  # "bab" or "aba"
print(longestPalindrome_bruteforce("cbbd"))   # "bb"


# ------------------------------------------------------------
# ## Two Pointers / Expand Around Center
# 1. Each character (and gap between characters) is a center.  
# 2. Expand left and right while s[l] == s[r].  
# 3. Track longest palindrome seen.  
#
# ⏱️ Time: O(n²)  
# 💾 Space: O(1)  
# ------------------------------------------------------------

class SolutionTwoPointers:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        start, end = 0, 0

        def expand(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return l+1, r-1

        for i in range(n):
            # Odd-length palindrome
            l1, r1 = expand(i, i)
            # Even-length palindrome
            l2, r2 = expand(i, i+1)
            if r1 - l1 > end - start:
                start, end = l1, r1
            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start:end+1]

# Test Two Pointers
sol = SolutionTwoPointers()
print(sol.longestPalindrome("babad"))  # "bab" or "aba"
print(sol.longestPalindrome("cbbd"))   # "bb"


# ============================================================
# 🧾 Summary
# ============================================================
# | Approach              | Time  | Space | Notes |
# |-----------------------|-------|-------|-----------------------------|
# | Brute Force           | O(n³) | O(1)  | Check all substrings        |
# | Two Pointers ✅        | O(n²) | O(1)  | Expand around center        |
# ============================================================
