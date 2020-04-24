class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = 0
        right = 0
        longestLen = 0
        charList = []
        
        while (right < len(s)):
            if (s[right] in charList):
                charList.remove(s[left])
                left = left + 1
            else:
                charList.append(s[right])
                longestLen = max(len(charList), longestLen)
                right = right + 1
        return longestLen
            
        
if __name__ == "__main__":
    # Test Cases
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))