# Input
employee_name = input("Enter employee name: ")
hourly_rate = float(input("Enter hourly rate ($): "))
hours_worked = float(input("Enter hours worked this week: "))
manager = input("Is the employee a manager? (yes/no): ").lower()

# Processing - Gross Pay with Overtime
if hours_worked <= 40:
    gross_pay = hourly_rate * hours_worked
else:
    gross_pay = (hourly_rate * 40) + ((hours_worked - 40) * hourly_rate * 1.5)

# Output
print("\nPayroll Summary")
print("Employee:", employee_name)
print("Hours Worked:", hours_worked)
print("Hourly Rate: $", format(hourly_rate, ".2f"))
print("Manager:", manager)
print("Gross Pay: $", format(gross_pay, ".2f"))