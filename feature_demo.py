def calculate_average(lst):
    """
    计算列表中所有元素的平均值。

    参数:
        lst (list): 包含数值（int 或 float）的列表

    返回:
        float: 列表中所有元素的平均值；如果列表为空，返回 0.0
    """
    if not lst:
        return 0.0
    return sum(lst) / len(lst)


if __name__ == '__main__':
    # 测试示例
    test_cases = [
        ([1, 2, 3, 4, 5], 3.0),
        ([2.5, 3.5], 3.0),
        ([], 0.0),
        ([10], 10.0),
        ([-1, 0, 1], 0.0),
    ]

    for nums, expected in test_cases:
        result = calculate_average(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {nums} -> {result} (期望: {expected})")