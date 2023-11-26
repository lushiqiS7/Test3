import Lab2

# Test Module for Lab2 Functions

# Display a message indicating the start of the test_Lab2
print("test_Lab2")

# Create a sample input array for testing
input_arr = [33, 22, 32, 35, 26, 28]

# Test function for find_min_max
def test_calc_min_max_temperature():
    """
    Test the find_min_max function in Lab2.
    """
    # Display a message indicating the start of the find_min_max test
    print("Testing find_min_max")

    # Define the expected result for find_min_max
    answer = [22, 35]

    # Call the find_min_max function from Lab2 with the input array
    result = Lab2.find_min_max(input_arr)

    # Check if the result matches the expected answer
    assert (result == answer)

# Test function for calc_average
def test_calc_average_temperature():
    """
    Test the calc_average function in Lab2.
    """
    # Display a message indicating the start of the calc_average test
    print("Testing calc_average")

    # Define the expected result for calc_average
    answer = 29.33333

    # Call the calc_average function from Lab2 with the input array
    result = Lab2.calc_average(input_arr)

    # Round the result to 5 decimal places before comparison
    result = round(result, 5)

    # Check if the result matches the expected answer
    assert (result == answer)

# Test function for calc_median_temperature
def test_calc_median_temperature():
    """
    Test the calc_median_temperature function in Lab2.
    """
    # Display a message indicating the start of the calc_median_temperature test
    print("Testing calc_median_temperature")

    # Define the expected result for calc_median_temperature
    answer = 30.00000

    # Call the calc_median_temperature function from Lab2 with the input array
    result = Lab2.calc_median_temperature(input_arr)

    # Round the result to 5 decimal places before comparison
    result = round(result, 5)

    # Check if the result matches the expected answer
    assert (result == answer)
