"""
直接插入排序
从下标为1的元素开始往前面插入
将下标为i的元素赋值给swap
如果下标为 i - 1 的元素大于 swap时 把该元素放到下标为i的位子，i - 1，直到 i == 0 或 ls[i - 1] < swap
浙江swap 放到i的位置
进行下一个元素插入
"""


def straight_insertion_sort(ls: list) -> list:
    for i in range(1, len(ls)):
        if ls[i - 1] < ls[i]:
            continue
        swap = ls[i]
        while i > 0 and ls[i - 1] > swap:
            ls[i] = ls[i - 1]
            i -= 1
        ls[i] = swap
    return ls
