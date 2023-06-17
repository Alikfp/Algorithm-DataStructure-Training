class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        score = 0
        nom = nums[0]
        for i in range(1, len(nums)):
            #print('score', score)
            #print('nom', nom)
            if nums[i] == nom:
                score += 1
            elif (score>0) and (nums[i] != nom):
                score -= 1
            else:
                score = 0
                nom = nums[i]
        return nom
                