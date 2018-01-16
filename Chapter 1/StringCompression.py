import unittest
def string_compression(s):
    prev = s[0]
    result = []
    count = 1
    for c in s[1:]:
        if prev == c:
            prev = c
            count += 1
        else:
            result.append(prev)
            result.append(str(count))
            prev = c
            count = 1
    result.append(prev)
    result.append(str(count))
    if len(s) * 2 == len(result):
        return s
    else:
        return ''.join(result)

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()

