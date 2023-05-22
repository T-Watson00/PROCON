from sys import stdin

def main() :
    nums :list = list(map(int,stdin.readline().split()))
    target : int = int(input())
    Problem_Input = Solution(nums,target)
    print(Problem_Input.two_sum())

class Solution:

    def __init__(self,nums:list[int],target: int):
        self.nums_list :list[int] = nums
        self.target :int = target

    def two_sum(self) -> list[int]:
        self.hash_map_already_investigated = dict()
        for index,num in enumerate(self.nums_list) :
            self.substract_to_target :int = self.target - num
            if self.substract_to_target in self.hash_map_already_investigated:
                return list([self.hash_map_already_investigated[self.substract_to_target],index])
            else :
                self.hash_map_already_investigated[num] = index


if __name__ == "__main__" :
    main()