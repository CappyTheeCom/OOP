import unittest
from task1 import Staff, Address  # Adjust import to your file/module name

class TestStaffMethods(unittest.TestCase):

    def setUp(self):
        self.address = Address(123,"main street","City", "state", 12345,"Country")
        self.staff = Staff("John","Doe", "1990-01-01", self.address, 000000, 52)
        Staff.staff_list.clear()
        Staff.staff_list.append(self.staff)
    
    def test_addstaff(self):
        self.assertIn(self.staff, Staff.staff_list)

    def test_searchstaff(self):
        self.assertIn(self.staff, Staff.staff_list)
        self.assertEqual(self.staff, )




if __name__ == '__main__':
    unittest.main()
