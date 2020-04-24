class Solution(object):
    def isPalindrome(self, x):
        strX = str(x)
        endIndex = len(strX) - (0 if (len(strX) % 2 == 0) else 1)
        for i in range(endIndex):
            if strX[i] != strX[len(strX) - i - 1]:
                return False
        return True


if __name__ == "__main__":
    # Test Cases
    print(Solution().isPalindrome(121))
    print(Solution().isPalindrome(121654654))
