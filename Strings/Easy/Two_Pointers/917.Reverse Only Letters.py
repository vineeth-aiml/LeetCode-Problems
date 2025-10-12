# ============================================================
# 917. Reverse Only Letters
# ============================================================

# 🧩 Problem:
# Given a string s, reverse only all the English letters in the string 
# and return it. 
#
# Non-letter characters (digits, symbols, etc.) remain in the same position.
#
# Letters include both lowercase and uppercase (a-z, A-Z).
#
# ------------------------------------------------------------
# Example 1:
# Input:  s = "ab-cd"
# Output: "dc-ba"
# Explanation:
# Letters ['a', 'b', 'c', 'd'] reversed → ['d', 'c', 'b', 'a'].
# Only letters swap places; '-' stays in the same position.
#
# Example 2:
# Input:  s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
#
# Example 3:
# Input:  s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# ------------------------------------------------------------
#
# Constraints:
# 1 <= len(s) <= 100
# s consists of ASCII characters in the range [33, 122].
# s does not contain " or \ characters.
# ------------------------------------------------------------


# ============================================================
# --- 1️⃣ Brute Force Solution ---
# ============================================================
# 🧠 Idea:
# 1. Extract all letters from s.
# 2. Reverse that list of letters.
# 3. Rebuild the string:
#    - If character is a letter, replace it with the next reversed letter.
#    - If not a letter, keep it as is.
#
# Steps:
# 1. Convert string to list for easy modification.
# 2. Collect all letters → reverse them.
# 3. Replace letters in order using reversed list.
# 4. Join and return the result.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(n)
# ------------------------------------------------------------

def reverseOnlyLetters(s):
    s_list = list(s)
    letters = []

    # Step 1: Collect all letters
    for ch in s_list:
        if ch.isalpha():
            letters.append(ch)

    # Step 2: Reverse collected letters
    letters.reverse()

    # Step 3: Replace only letter positions
    j = 0
    for i in range(len(s_list)):
        if s_list[i].isalpha():
            s_list[i] = letters[j]
            j += 1

    # Step 4: Join list → string
    return "".join(s_list)


# Test
s = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(s))  # ✅ "j-Ih-gfE-dCba"



# ============================================================
# --- 2️⃣ Two Pointers Solution (Optimized) ---
# ============================================================
# 🧠 Idea:
# Use two pointers (left and right) to swap letters directly in place.
# Skip non-letter characters.
#
# Steps:
# 1. Convert s to list for mutability.
# 2. Initialize two pointers:
#       left = 0
#       right = len(s_list) - 1
# 3. While left < right:
#       - Move left forward if not a letter.
#       - Move right backward if not a letter.
#       - If both are letters, swap them.
#       - Move both pointers inward.
# 4. Join and return the final string.
#
# ✅ No need to store extra arrays.
#
# ⏱️ Time:  O(n)
# 💾 Space: O(1)   (ignoring string → list conversion)
# ------------------------------------------------------------

def reverseOnlyLetters(s):
    s_list = list(s)
    l, r = 0, len(s_list) - 1

    while l < r:
        # Skip non-letters from left
        if not s_list[l].isalpha():
            l += 1
            continue

        # Skip non-letters from right
        if not s_list[r].isalpha():
            r -= 1
            continue

        # Swap letters
        s_list[l], s_list[r] = s_list[r], s_list[l]

        # Move inward
        l += 1
        r -= 1

    return "".join(s_list)


# Test
s = "Test1ng-Leet=code-Q!"
print(reverseOnlyLetters(s))  # ✅ "Qedo1ct-eeLg=ntse-T!"



# ============================================================
# 🧾 Summary Comparison
# ============================================================
# | Approach       | Time      | Space | Notes |
# |----------------|-----------|--------|--------|
# | Brute Force    | O(n)      | O(n)   | Collect & rebuild |
# | Two Pointers   | O(n)      | O(1)   | ✅ Best & in-place |
# ============================================================
