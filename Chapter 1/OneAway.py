import unittest
def is_one_away(s1, s2):
    if len(s1) == len(s2):
        return is_replace(s1, s2)
    elif len(s1)+1 == len(s2):
        return is_update(s2,s1)
    elif len(s1) == len(s2)+1:
        return is_update(s1,s2)
    else:
        return False

def is_replace(s1, s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            pass
        else:
            count += 1
            if count == 2:
                return False
    return True

def is_update(s1, s2):
    count = 0
    j=0
    for i in range(len(s1)):
        if j < len(s2):
            if s1[i] == s2[j]:
                j += 1
            else:
                count += 1
                if count == 2:
                    return False
    return True

class Test(unittest.TestCase):
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = is_one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
