class Solution:
    "Given an array of integers, return indices of the two numbers such that they add up to a specific target."
    def twoSum(self, nums: List[int], target: int) -> List[int]:
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
            nums = stringToIntegerList(line);
            line = next(lines)
            target = int(line);
            
            ret = Solution().twoSum(nums, target)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()
