class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        num1, num2 = 0, len(numbers)-1

        while num2 > num1:
            #print(num1, num2)
            if (numbers[num1] + numbers[num2]) > target:
                num2 -= 1
            elif (numbers[num1] + numbers[num2]) < target:
                num1 += 1
            else:
                return [num1+1, num2+1]
