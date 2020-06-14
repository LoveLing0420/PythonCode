import random

'''
冒泡排序算法
例如有长度为17的list如下（下标为0-16）：
[173, 89, 52, 12, 131, 106, 26, 176, 74, 120, 118, 188, 57, 191, 196, 33, 140]
起始记录最高下标16，对下标0-15的数与它的next进行比较，如果next小于它，则调换位置，并记录当前下标为下一次循环的最高下标
最高下标后面的数都大于最高下标以及其前面的数，而且是升序排序
所以下次循环只用判断到最高下标就行
当最高下标为0是，整个list排序完毕
'''


def bubble_sort(ls: list) -> list:
    highest = len(ls) - 1
    while highest:
        next_highest = 0
        for i in range(highest):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                next_highest = i
        highest = next_highest
    return ls


if __name__ == '__main__':
    for m in range(10000):
        test_ls = []
        for n in range(random.randint(0, 200)):
            test_ls.append(random.randint(0, 2000))
        test_ls = bubble_sort(test_ls)
        for k in range(len(test_ls) - 1):
            if test_ls[k] > test_ls[k + 1]:
                raise Exception('Sort Error')
