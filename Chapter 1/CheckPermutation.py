import unittest

def check_permutation1(str1, str2):
    if len(str1) != len(str2):
        return False
    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True

def check_permutation(str1,str2):
    dict = {}
    if len(str1) != len(str2):
        return False
    for each in str1:
        dict[each] += 1
    for each in str2:
        dict[each] -= 1
    for key in dict.keys():
        if dict[key] != 0 :
            return False
    return True

class Test(unittest.TestCase):
    dataTrue = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataFalse = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )
    def test_check_permutation(self):
        for each in self.dataTrue:
            self.assertTrue(check_permutation(each[0],each[1]))
        for each in self.dataFalse:
            self.assertFalse(check_permutation,each[0],each[1])

if __name__ == '__main__':
    unittest.main()
