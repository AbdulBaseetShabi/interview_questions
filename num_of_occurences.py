# 0(n) runtime 
def num_of_occurences(string):
    occurences = {}
    for i in string:
        lower_i = i.lower()
        try:
            occurences[lower_i] += 1
        except:
            occurences[lower_i] = 1
    return occurences

# 0(n^2) runtime 
def num_of_occurences_alt(string):
    occurences = {}
    for i in string:
        lower_i = i.lower()
        if lower_i in occurences:
            occurences[lower_i] += 1
        else:
            occurences[lower_i] = 1
    return occurences


if __name__ == '__main__':
    print("Testing Number of Occurences Problem: ")
    test1 = num_of_occurences("aaaabbbb")
    print("string = 'aaaabbbb', passed: {}".format(test1['a'] == 4 and test1['b'] == 4 and len(test1) == 2))
    test2 = num_of_occurences("abCCccc")
    print("string = 'abccccc', passed: {}".format(test2['a'] == 1 and test2['b'] == 1 and test2['c'] == 5 and len(test2) == 3))
    test3 = num_of_occurences("abcdbb")
    print("string = \"abcdbb\", passed: {}".format((test3['a'] == 1 and test3['b'] == 3 and test3['c'] == 1 and test3['d'] == 1) and len(test3) == 4))
    test4 = num_of_occurences("")
    print("string = \"\", passed: {}".format(len(test4) == 0))
    print("Test Done")