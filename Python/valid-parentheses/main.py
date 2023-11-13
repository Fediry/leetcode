class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = ['(', ')', '[', ']', '{', '}']
        print(str(parentheses))

test = "()"
solution = Solution()
print(solution.isValid(test))