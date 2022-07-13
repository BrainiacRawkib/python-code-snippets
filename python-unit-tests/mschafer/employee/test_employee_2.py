import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.emp_1 = Employee('Brainiac', 'Rawkib', 500000)
        self.emp_2 = Employee('Brainy', 'Rawkeeb', 600000)

    def tearDown(self) -> None:
        pass

    def test_email(self):
        self.assertEqual(self.emp_1.email, 'Brainiac.Rawkib@email.com')
        self.assertEqual(self.emp_2.email, 'Brainy.Rawkeeb@email.com')

        self.emp_1.first = 'Adam'
        self.emp_2.first = 'Kareem'

        self.assertEqual(self.emp_1.email, 'Adam.Rawkib@email.com')
        self.assertEqual(self.emp_2.email, 'Kareem.Rawkeeb@email.com')

    def test_fullname(self):
        self.assertEqual(self.emp_1.fullname, 'Brainiac Rawkib')
        self.assertEqual(self.emp_2.fullname, 'Brainy Rawkeeb')

        self.emp_1.first = 'Adam'
        self.emp_2.first = 'Kareem'

        self.assertEqual(self.emp_1.fullname, 'Adam Rawkib')
        self.assertEqual(self.emp_2.fullname, 'Kareem Rawkeeb')

    def test_apply_raise(self):
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 525000)
        self.assertEqual(self.emp_2.pay, 630000)


if __name__ == '__main__':
    unittest.main()
