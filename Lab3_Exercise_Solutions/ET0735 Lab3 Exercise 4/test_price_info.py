# Import the 'price_info' module for testing.
import price_info

# Print a message to indicate that this script is testing the 'price_info' module.
print("test_price_info")

# Test function for 'total_cost_shopping' in 'price_info' module.
def test_total_cost_shopping():
    # Print an empty line for better readability in the console.
    print("")
    
    # Define the expected result for the 'total_cost_shopping' function.
    answer = 46.75
    
    # Call the 'total_cost_shopping' function and store the result.
    result = price_info.total_cost_shopping()
    
    # Compare the result with the expected answer using the 'assert' statement.
    assert result == answer

# Test function for 'cost_of_fruits' in 'price_info' module.
def test_cost_of_fruits():
    # Print an empty line for better readability in the console.
    print("")
    
    # Define the expected result for the 'cost_of_fruits' function.
    answer = 12.0
    
    # Call the 'cost_of_fruits' function with parameters and store the result.
    result = price_info.cost_of_fruits('apple', 10)
    
    # Compare the result with the expected answer using the 'assert' statement.
    assert result == answer
