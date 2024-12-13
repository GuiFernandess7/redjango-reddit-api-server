from django.db import models

class Employee(models.Model):
    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]

    emp_id = models.BigIntegerField(primary_key=True, verbose_name="Employee ID")
    first_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="First Name")
    last_name = models.CharField(max_length=100, blank=False, null=False, verbose_name="Last Name")
    birth_date = models.DateField(blank=False, null=False, verbose_name="Birth Date")
    sex = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False, null=False, verbose_name="Sex")
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False, verbose_name="Salary")
    supervisor = models.ForeignKey("Employee", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Supervisor")
    branch = models.ForeignKey("Branch", on_delete=models.CASCADE, blank=True, null=True, verbose_name="Branch")  # Modificado para permitir null

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Branch(models.Model):
    class Meta:
        verbose_name = "Branch"
        verbose_name_plural = "Branches"

    branch_id = models.BigIntegerField(primary_key=True, verbose_name="Branch ID")
    branch_name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Branch Name")
    mmanager = models.OneToOneField(Employee, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Manager", related_name="branch_manager")  # Modificado para permitir null
    manager_start_date = models.DateField(null=False, blank=False, verbose_name="Manager Start Date")

    def __str__(self):
        return self.branch_name

class Client(models.Model):
    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    client_id = models.BigIntegerField(primary_key=True, verbose_name="Client ID")
    client_name = models.CharField(max_length=150, blank=False, null=False, verbose_name="Client Name")
    branch = models.ForeignKey(Branch, blank=False, null=False, on_delete=models.CASCADE)

class WorksWith(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, null=False, blank=False)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE, blank=False, null=False)
    total_sales = models.FloatField(blank=False, null=False)

    class Meta:
        unique_together = ('employee_id', 'client_id')

class BranchSupplier(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, blank=False, null=False)
    supplier_name = models.CharField(blank=False, null=False, max_length=150)
    supply_type = models.CharField(blank=False, null=False, max_length=150)

    class Meta:
        unique_together = ('branch', 'supplier_name')