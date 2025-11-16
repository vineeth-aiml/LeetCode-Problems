# 344. Reverse String
# Problem:
# Reverse the given character array in-place.
# Must do it with O(1) extra memory.

# --- Brute Force ---
# Steps:
# 1. Create an empty list
# 2. Traverse the array from end to start
# 3. Append each element to the new list
# 4. Copy back into the original array
# Time: O(n), Space: O(n)

def reverseString(s):
    n = len(s)
    ans = []
    for i in range(n-1, -1, -1):
        ans.append(s[i])
    for i in range(n):
        s[i] = ans[i]

s = ["h","e","l","l","o"]
reverseString(s)
print(s)

# --- Two Pointers ---
# Steps:
# 1. Initialize left = 0, right = len(s)-1
# 2. While left < right:
#    - Swap s[left] and s[right]
#    - Move left++, right--
# Time: O(n), Space: O(1)

def reverseString(s):
    l = 0  # left from zero
    r = len(s)-1  # right from end of array
    while l < r:  # while meet l and r
        s[l], s[r] = s[r], s[l] # swap two ends
        l += 1 # move left to right after swap 
        r -= 1 # move right to left after swap
s = ["H","a","n","n","a","h"]
reverseString(s)
print(s)
