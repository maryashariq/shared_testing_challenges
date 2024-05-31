from lib.high_value import *

"""
Test that self.value_first and self.value_second are
being assigned correctly
"""

def test_value_first_is_being_assigned_correctly():
    high_value_object = HighValue(7, 12)
    assert high_value_object.value_first == 7

def test_value_second_is_being_assigned_correctly():
    high_value_object = HighValue(7, 12)
    assert high_value_object.value_second == 12

def test_value_get_highest_valuefirst_greater_than_valuesecond():
    high_value_object = HighValue(24,15)
    assert high_value_object.get_highest() == "First value is higher"

""""
Testing what happens when self.value_second is higher than self.value_first
"""

def test_value_get_highest_valuesecond_greater_than_valuefirst():
    high_value_object = HighValue(17, 94)
    assert high_value_object.get_highest() == "Second value is higher"

""""
Testing when self.value_first and self.value_second are equal
"""

def test_values_are_equal():
    high_value_object = HighValue(5,5)
    assert high_value_object.get_highest() == "Values are equal"

"""
Testing if 'increase_by' and 'selection_first' returns self.value_first + increase_by
"""

def test_add_selection_first_value():
    high_value_object = HighValue(34, 16)
    high_value_object.add(6, "first")
    assert high_value_object.value_first == 40

"""
Testing if 'increase_by' and 'selection_second' returns self.value_second + increase_by
"""

def test_add_selection_second_value():
    high_value_object = HighValue(20, 6)
    high_value_object.add(4, "second")
    assert high_value_object.value_second == 10

