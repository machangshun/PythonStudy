'''
Leedcode 1.两数之和
'''
class Solution():
    '''我的'''
    # def twoSum(self,nums,target):
    #     q = 0
    #     for t in range(1,len(nums)):
    #         for i in range(t, len(nums)):
    #             if nums[q] + nums[i] == target:
    #                 return [q, i]
    #         else:
    #             q += 1
    '''大神的'''
    def twoSum(self,nums,target):
        dct = {}
        for i,n in enumerate(nums):
            if target - n in dct:
                return [dct[target-n],i]
            dct[n] = i
            print(dct)
if __name__ == '__main__':
    s = Solution()
    nums = []
    for i in range(0,int(input())):
        nums.append(int(input()))
    target = int(input())
    print(s.twoSum(nums,target))
