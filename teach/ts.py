
def two_sum(nums,target):
    dictionary = {}
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in dictionary:
            return [dictionary[diff],i]
        dictionary[nums[i]] = i

if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9

    

    print(two_sum(nums,target))
