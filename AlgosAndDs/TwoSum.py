from typing import List
import json
class Solution:
    def two_sum(self,nums,target):
        map = {}
        for i,val in enumerate(nums):
            if -val in map:
               return [map[-val],i]
            else:
                map[val-target] = i
                
        return [0,0]

def stringToIntegerList(input):
    return json.loads(input)

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line)
            line = next(lines)
            target = int(line)
            
            ret = Solution().two_sum(nums, target)

            out = integerListToString(ret)
            print(out)
        except StopIteration:
            break

print(Solution().two_sum([1,2,4,5],9))