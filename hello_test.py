'''Test for hello module
'''
import hello
import unittest


class HelloTest(unittest.TestCase):
    '''as'''

    def test_can_say_hello_to_eve(self):
        self.assertEqual(hello.say_hello('Eve'), 'Hello, Eve')

    def test_foo(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
