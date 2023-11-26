import employee_info

# Print a message indicating the start of testing
print("test_employee_info")

# Test case 1: get_employees_by_age_range with age range (21, 31)
def test_get_employees_by_age_range1():
    result = []
    # Define the expected answer as a slice of the first three elements
    answer = employee_info.employee_data[0:3]
    # Call the function with the specified age range
    result = employee_info.get_employees_by_age_range(21, 31)
    # Assert that the result matches the expected answer
    assert (result == answer)

# Test case 2: get_employees_by_age_range with age range (29, 36)
def test_get_employees_by_age_range2():
    result = []
    # Create an answer list using a list comprehension to select specific elements
    answer = [employee_info.employee_data[index] for index in [0, 3, 4]]
    # Call the function with the specified age range
    result = employee_info.get_employees_by_age_range(29, 36)
    # Assert that the result matches the expected answer
    assert (result == answer)

# Test case 3: calculate_average_salary
def test_calculate_average_salary():
    # Define the expected average salary
    answer = 60166.67
    # Call the function to calculate the average salary
    result = employee_info.calculate_average_salary()
    # Assert that the result matches the expected answer
    assert (result == answer)

# Test case 4: get_employees_by_dept with department 'Marketing'
def test_get_employees_by_dept1():
    result = []
    # Define the expected answer as a slice of elements for the 'Marketing' department
    answer = employee_info.employee_data[1:3]
    # Call the function with the specified department
    result = employee_info.get_employees_by_dept('Marketing')
    # Assert that the result matches the expected answer
    assert (result == answer)

# Test case 5: get_employees_by_dept with department 'Sales'
def test_get_employees_by_dept2():
    result = []
    # Create an answer list using a list comprehension to select specific elements -1 is the last element

    answer = [employee_info.employee_data[index] for index in [0, -1]]
    # Call the function with the specified department
    result = employee_info.get_employees_by_dept('Sales')
    # Assert that the result matches the expected answer
    assert (result == answer)
