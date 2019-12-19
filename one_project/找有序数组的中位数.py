# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

# 你可以假设 nums1 和 nums2 不会同时为空。

# nums1 = [1, 2]
# nums2 = [3, 4]

# 则中位数是 (2 + 3)/2 = 2.5


nums1 = [1, 3, 5]
nums2 = [4, 6, 7, 8]

nums = nums1+nums2

nums.sort()

if not len(nums) % 2:
    print('111')

    num = (nums[(len(nums) // 2) - 1] + nums[(len(nums) // 2)]) / 2
    print(num)
else:

    num = nums[((len(nums) + 1) // 2) - 1]
    # num = len(nums)+1

    print(num)


print(nums)
