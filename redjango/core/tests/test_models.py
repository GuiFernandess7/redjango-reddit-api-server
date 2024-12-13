from django.test import TestCase
from django.core.exceptions import ValidationError
from core.models import Branch, Employee

import datetime

class BranchModelTest(TestCase):
    def setUp(self):
        manager_start_date = datetime.date(2020, 1, 1)

        branch = Branch.objects.create(
            branch_id=1,
            branch_name="Scranton",
            manager_start_date="2024-01-01"
        )

        employee = Employee.objects.create(
            emp_id=1,
            first_name="Michael",
            last_name="Scott",
            birth_date="1980-01-01",
            sex="M",
            salary=60000.00,
            branch=branch
        )

        branch.mmanager = employee
        branch.save()

    def test_branch_createtion(self):
        self.assertEqual(self.branch.branch_name, "Scranton")
        self.assertEqual(self.branch.mmanager, "Michael Scott")
        self.assertEqual(self.branch.manager_start_date, datetime.date(2020, 1, 1))