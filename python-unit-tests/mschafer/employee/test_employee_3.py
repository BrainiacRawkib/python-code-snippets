import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('setupClass')

    @classmethod
    def tearDownClass(cls) -> None:
        print('tearDownClass')

    def setUp(self) -> None:
        print('setUp')
        self.emp_1 = Employee('Brainiac', 'Rawkib', 500000)
        self.emp_2 = Employee('Brainy', 'Rawkeeb', 600000)

    def tearDown(self) -> None:
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Brainiac.Rawkib@email.com')
        self.assertEqual(self.emp_2.email, 'Brainy.Rawkeeb@email.com')

        self.emp_1.first = 'Adam'
        self.emp_2.first = 'Kareem'

        self.assertEqual(self.emp_1.email, 'Adam.Rawkib@email.com')
        self.assertEqual(self.emp_2.email, 'Kareem.Rawkeeb@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Brainiac Rawkib')
        self.assertEqual(self.emp_2.fullname, 'Brainy Rawkeeb')

        self.emp_1.first = 'Adam'
        self.emp_2.first = 'Kareem'

        self.assertEqual(self.emp_1.fullname, 'Adam Rawkib')
        self.assertEqual(self.emp_2.fullname, 'Kareem Rawkeeb')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 525000)
        self.assertEqual(self.emp_2.pay, 630000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Rawkib/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('http://company.com/Rawkeeb/June')

            self.assertEqual(schedule, 'Bad Response!')


if __name__ == '__main__':
    unittest.main()
