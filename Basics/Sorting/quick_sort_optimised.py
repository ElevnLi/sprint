def partition(nums: list[int], left: int, right: int) -> int:
    """哨兵划分"""
    # 以 nums[left] 为基准数
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= nums[left]:
            j -= 1  # 从右向左找首个小于基准数的元素
        while i < j and nums[i] <= nums[left]:
            i += 1  # 从左向右找首个大于基准数的元素
        # 元素交换
        nums[i], nums[j] = nums[j], nums[i]
    # 将基准数交换至两子数组的分界线
    nums[i], nums[left] = nums[left], nums[i]
    return i  # 返回基准数的索引


def quick_sort_optimised_recursion(nums: list[int], left: int, right: int):
    """快速排序（尾递归优化）"""
    # 子数组长度为 1 时终止
    while left < right:
        # 哨兵划分操作
        pivot = partition(nums, left, right)
        # 对两个子数组中较短的那个执行快速排序
        if pivot - left < right - pivot:
            quick_sort_optimised_recursion(nums, left, pivot - 1)  # 递归排序左子数组
            left = pivot + 1  # 剩余未排序区间为 [pivot + 1, right]
        else:
            quick_sort_optimised_recursion(nums, pivot + 1, right)  # 递归排序右子数组
            right = pivot - 1  # 剩余未排序区间为 [left, pivot - 1]


def sort(nums: list[int]):
    quick_sort_optimised_recursion(nums, 0, len(nums) - 1)
