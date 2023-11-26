import Lab3_Exercise2 as Lab3ex2

# Display a message indicating the start of the test_Lab3_Exercise2
print("test_Lab3_Exercise2")

# Constants for sorting order
SORT_ASCENDING_ORDER = 0
SORT_DESCENDING_ORDER = 1

# REQ-01 Test sorting in ascending order
def test_Sort_Ascending_Order():
    print("")  # Print an empty line for better readability
    result = []  # Initialize the result variable
    input_arr = [3, 2, 1, 6, 7, 4, 5]  # Input array for testing
    answer = [1, 2, 3, 4, 5, 6, 7]  # Expected result after sorting in ascending order
    
    # Call the bubble_sort function from Lab3ex2 to sort the array in ascending order
    result = Lab3ex2.bubble_sort(input_arr, SORT_ASCENDING_ORDER)
    
    # Check if the result matches the expected answer
    assert (result == answer)


# REQ-02 Test sorting in descending order
def test_Sort_Descending_Order():
    print("")  # Print an empty line for better readability
    result = []  # Initialize the result variable
    input_arr = [3, 2, 1, 6, 7, 4, 5]  # Input array for testing
    answer = [7, 6, 5, 4, 3, 2, 1]  # Expected result after sorting in descending order
    
    # Call the bubble_sort function from Lab3ex2 to sort the array in descending order
    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING_ORDER)
    
    # Check if the result matches the expected answer
    assert (result == answer)


# REQ-03 Test array with >= 10 elements
def test_Long_array():
    print("")  # Print an empty line for better readability
    input_arr = [3, 10, 2, 1, 8, 9, 6, 7, 4, 5]  # Input array with 10 elements
    answer = 1  # Expected result after sorting in descending order
    
    # Call the bubble_sort function from Lab3ex2 to sort the array in descending order
    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING_ORDER)
    
    # Check if the result matches the expected answer
    assert (result == answer)


# REQ-04 Test array with no element (i.e., empty array).
def test_Empty_array():
    print("")  # Print an empty line for better readability
    input_arr = []  # Empty input array
    answer = 0  # Expected result for an empty array
    
    # Call the bubble_sort function from Lab3ex2 to sort the array in descending order
    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING_ORDER)
    
    # Check if the result matches the expected answer
    assert (result == answer)


# REQ-05 Test array with non-integer element(s).
def test_Not_pure_integer_array():
    print("")  # Print an empty line for better readability
    input_arr = [3, 2, 1, 6, 7.7, 4, 5]  # Input array with a non-integer element
    answer = 2  # Expected result after sorting in descending order
    
    # Call the bubble_sort function from Lab3ex2 to sort the array in descending order
    result = Lab3ex2.bubble_sort(input_arr, SORT_DESCENDING_ORDER)
    
    # Check if the result matches the expected answer
    assert (result == answer)
