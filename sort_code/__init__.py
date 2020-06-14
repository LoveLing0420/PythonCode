import random
if __name__ == '__main__':
    for m in range(1000):
        test_ls: list = []
        for n in range(random.randint(0, 200)):
            test_ls.append(random.randint(0, 2000))
        test_ls = sort_code(test_ls)
        for k in range(len(test_ls) - 1):
            if test_ls[k] > test_ls[k + 1]:
                raise Exception('Sort Error')
