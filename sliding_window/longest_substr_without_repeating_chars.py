def lengthOfLongestSubstring(s):
    # brute force > check every substring -> n^2
    # optimal > sliding window - O(N)
    charSet = set()

    # basic template of sliding window 
        # initialize a set that ensure we don't have duplicates in our current window
        # have a start pointer and run the loop with end pointer starting from 0 till len of arr/string
        # check if the character at end is already present:
            # if yes, remove characters from set from the start of the window, until the window has no dups
            # keep moving your start pointer ahead
        # now you add the character at the end because you have removed any occurence of that char in the window
        # update max 
        # return max


    ws = 0
    maxi = 0
    for we in range(len(s)):
        while s[we] in charSet:
            charSet.remove(s[ws])
            ws += 1
        charSet.add(s[we])
        maxi = max(maxi, we - ws + 1)

    return maxi
        
