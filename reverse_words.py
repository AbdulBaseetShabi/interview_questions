def reverse_words(string):
    string_array = string.split(" ")
    string_array = string_array[::-1]
    return " ".join(string_array)

if __name__ == '__main__':
    print("Testing Reverse Words Problem: ")
    test1 = reverse_words("This is a test")
    print("string = 'This is a test', passed: {}".format(test1 == "test a is This"))
    test2 = reverse_words("")
    print("string = '', passed: {}".format(test2 == ""))
    test3 = reverse_words("why is")
    print("string = \"why is\", passed: {}".format(test3 == "is why"))
    test4 = reverse_words("let us    meet up")
    print("string = \"let us    meet up\", passed: {}".format(test4 == "up meet    us let"))
    print("Test Done")