# ============================================================
# 345. Reverse Vowels of a String
# ============================================================

# ## Problem
# Given a string `s`, reverse only the vowels in the string and return it.
#
# The vowels are: `'a', 'e', 'i', 'o', 'u'` (both lowercase and uppercase).
#
# ------------------------------------------------------------
# ## Examples
# Input:  s = "IceCreAm"
# Output: "AceCreIm"
# Explanation:
#   Vowels in s: ['I', 'e', 'e', 'A'] → after reversing → ['A', 'e', 'e', 'I']
#   Resulting string = "AceCreIm"
#
# Input:  s = "leetcode"
# Output: "leotcede"
#
# ------------------------------------------------------------
# ## Constraints
# 1 <= len(s) <= 3 * 10^5
# s consists of printable ASCII characters.
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Approach ---
# ============================================================
# 🧠 Idea:
# Extract all vowels, reverse them, and then reinsert them
# back into their positions in the original string.
#
# ------------------------------------------------------------
# Steps:
# 1. Create a set of vowels for O(1) lookup.
# 2. Convert string → list (because strings are immutable).
# 3. Collect all vowels in a separate list.
# 4. Reverse that vowel list.
# 5. Traverse the string list again:
#    - When a vowel is found, replace it with next reversed vowel.
# 6. Join the list back into a string and return it.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def reverseVowels(s):
    vowels = set("aeiouAEIOU")        # Step 1: define vowels
    s_list = list(s)                   # Step 2: make mutable list
    vowel_chars = [ch for ch in s_list if ch in vowels]  # Step 3
    vowel_chars.reverse()              # Step 4
    j = 0                              # Step 5: pointer for reversed vowels

    for i in range(len(s_list)):       # Step 6
        if s_list[i] in vowels:
            s_list[i] = vowel_chars[j]
            j += 1

    return "".join(s_list)             # Step 7

# Test
print(reverseVowels("IceCreAm"))   # ✅ AceCreIm
print(reverseVowels("leetcode"))   # ✅ leotcede


# ============================================================
# --- 2️⃣ Two Pointers Approach (Optimal) ---
# ============================================================
# 🧠 Idea:
# Use two pointers: one from start, one from end.
# Swap vowels when both sides have vowels, and move inward.
#
# ------------------------------------------------------------
# Steps:
# 1. Initialize left = 0, right = len(s)-1.
# 2. While left < right:
#    - Move left forward until s[left] is a vowel.
#    - Move right backward until s[right] is a vowel.
#    - Swap the vowels.
#    - Move both pointers inward.
# 3. Return the modified string.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1)
# ------------------------------------------------------------

def reverseVowels(s):
    vowels = set("aeiouAEIOU")
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        # Move left pointer until a vowel is found
        while left < right and s_list[left] not in vowels:
            left += 1
        # Move right pointer until a vowel is found
        while left < right and s_list[right] not in vowels:
            right -= 1
        # Swap the vowels
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    return "".join(s_list)

# Test
print(reverseVowels("IceCreAm"))   # ✅ AceCreIm
print(reverseVowels("leetcode"))   # ✅ leotcede


# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach       | Time   | Space | Notes |
# |----------------|--------|--------|-----------------------------|
# | Brute Force    | O(n)   | O(n)  | Easier to understand        |
# | Two Pointers   | O(n)   | O(1)  | ✅ Best performance, optimal |
# ============================================================
