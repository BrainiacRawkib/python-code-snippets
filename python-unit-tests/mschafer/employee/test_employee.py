import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    def test_email(self):
        emp_1 = Employee('Brainiac', 'Rawkib', 500000)
        emp_2 = Employee('Brainy', 'Rawkeeb', 600000)

        self.assertEqual(emp_1.email, 'Brainiac.Rawkib@email.com')
        self.assertEqual(emp_2.email, 'Brainy.Rawkeeb@email.com')

        emp_1.first = 'Adam'
        emp_2.first = 'Kareem'

        self.assertEqual(emp_1.email, 'Adam.Rawkib@email.com')
        self.assertEqual(emp_2.email, 'Kareem.Rawkeeb@email.com')

    def test_fullname(self):
        emp_1 = Employee('Brainiac', 'Rawkib', 500000)
        emp_2 = Employee('Brainy', 'Rawkeeb', 600000)

        self.assertEqual(emp_1.fullname, 'Brainiac Rawkib')
        self.assertEqual(emp_2.fullname, 'Brainy Rawkeeb')

        emp_1.first = 'Adam'
        emp_2.first = 'Kareem'

        self.assertEqual(emp_1.fullname, 'Adam Rawkib')
        self.assertEqual(emp_2.fullname, 'Kareem Rawkeeb')

    def test_apply_raise(self):
        emp_1 = Employee('Brainiac', 'Rawkib', 500000)
        emp_2 = Employee('Brainy', 'Rawkeeb', 600000)

        emp_1.apply_raise()
        emp_2.apply_raise()

        self.assertEqual(emp_1.pay, 525000)
        self.assertEqual(emp_2.pay, 630000)


if __name__ == '__main__':
    unittest.main()
