import unittest

def urlify(inp_str, inp_len):
    op_str = inp_str.split()[0]
    for word in inp_str.split()[1:]:
        op_str += '%20' +word
    return op_str

class Test():
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]
    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string,length)
            self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
