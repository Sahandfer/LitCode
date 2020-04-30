class Solution(object):
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''

if __name__ == "__main__":
    # Test Cases
    print(Solution().isValid("()"))
    print(Solution().isValid("({})"))