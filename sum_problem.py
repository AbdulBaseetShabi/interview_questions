def sum_problem(n):
    sum = 0
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            continue
        elif i % 3 == 0 or i % 5 ==0:
            sum += i
    return sum


if __name__ == '__main__':
    print("Testing Sum Problem: ")
    test1 = sum_problem(1)
    print("n = 1, passed: {}".format(test1 == 0))
    test2 = sum_problem(5)
    print("n = 5, passed: {}".format(test2 == 8))
    test3 = sum_problem(15)
    print("n = 15, passed: {}".format(test3 == (3 + 5 + 6 + 9 + 10 + 12)))
    test4 = sum_problem(20)
    print("n = 20, passed: {}".format(test4 == (3 + 5 + 6 + 9 + 10 + 12 + 18 + 20)))
    print("Test Done")