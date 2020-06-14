import queue

"""
快速排序算法
排序对象长度小于2，直接放回
用一个队列记录要排序的最第低下标和最高下标，队列为空，则排序完成
用low，high指向最低、最高下标，swap指向排序范围的第一个元素
当high > low时
Ⅰ、从high位置开始找，判断该位置的数是否大于swap元素，是则high - 1，否则把high位置元素放到low位置，low + 1，
Ⅱ、从low位置开始找，判断该位置的数是否小于swap元素，是则low + 1，否则把low位置元素放到high位置，high - 1，
重复Ⅰ、Ⅱ直到high == low
如果low - 1 > 最底下标，则将 最低下标 和 low - 1 作为排序范围加入队列
如果high + 1 < 最高下标，则将 high + 1 和 最高下标 作为排序访问加入队列
直到队列为空，排序完成
"""


def quick_sort(ls: list) -> list:
    if len(ls) < 2:
        return ls
    sort_queue = queue.Queue()
    sort_queue.put((0, len(ls) - 1))
    while not sort_queue.empty():
        sort_range = sort_queue.get()
        low, high = sort_range[0], sort_range[1]
        swap = ls[low]
        flags = True
        while low < high:
            if flags:
                if ls[high] >= swap:
                    high -= 1
                else:
                    ls[low] = ls[high]
                    low += 1
                    flags = False
            else:
                if ls[low] <= swap:
                    low += 1
                else:
                    ls[high] = ls[low]
                    high -= 1
                    flags = True
        ls[low] = swap
        if low - 1 > sort_range[0]:
            sort_queue.put((sort_range[0], low - 1))
        if high + 1 < sort_range[1]:
            sort_queue.put((high + 1, sort_range[1]))
    return ls
