mapping = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'mno',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz'
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        if len (digits) == 1:
            return list(mapping[digits[0]])

        curr_letters = list(mapping[digits[-1]])
        previous = self.letterCombinations(digits[:-1])
        return [ p + curr for p in previous for curr in curr_letters]