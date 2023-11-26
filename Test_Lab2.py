from Test2.lab2 import find_min_max, calc_average, calc_median_temperature


def test_find_min_max():
    # Test case 1: Non-empty list
    temperature_list = [25.5, 30.0, 20.0, 15.5, 18.0]
    expected_min = 15.5
    expected_max = 30.0
    min_temp, max_temp = find_min_max(temperature_list)
    assert min_temp == expected_min
    assert max_temp == expected_max


def test_calc_average():
    temperature_list = [25.5, 30.0, 20.0, 15.5, 18.0]
    avg = 21.8
    avg_temp = calc_average(temperature_list)
    assert avg_temp == avg


def test_calc_median_temperature():
    temperature_list = [25.5, 30.0, 20.0, 15.5, 18.0]
    median = 20
    med_temp = calc_median_temperature(temperature_list)
    assert med_temp == median
