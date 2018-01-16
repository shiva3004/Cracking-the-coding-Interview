import unittest
def is_unique(string):
    if len(string) > 128:
        return False
    char_vector = [False for i in range(128)]
    for each in string:
        val = ord(each)
        if char_vector[val]:
            return False
        else:
            char_vector[val] = True
    return True

class Test(unittest.TestCase):
    dataTrue = [('abcd'),(''),('4rtgfs')]
    dataFalse = [('sayfhu6s'),('sfj *((')]

    def test_unique(self):
        for str in self.dataTrue:
            self.assertTrue(is_unique(str))
        for str in self.dataFalse:
            self.assertFalse(is_unique(str))

if __name__ == '__main__':
    unittest.main()
