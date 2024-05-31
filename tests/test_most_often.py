from lib.most_often import *

""""
This function tests if def_init is correctly
creating a list
"""

def test_starting_list_is_being_created_correctly():
    most_often_object = MostOften([1, 1, 1, 3, 3, 3, 2])
    assert most_often_object.starting_list == [1, 1, 1, 3, 3, 3, 2]

""""
This function tests if add is correctly
adding a new item to our existing list
"""

def test_adding_new_object_to_list():
    most_often_object = MostOften([1, 1, 1, 3, 3, 3, 2])
    new_item = 6
    most_often_object.add_new(new_item)
    assert most_often_object.starting_list == [1, 1, 1, 3, 3, 3, 2, 6]

""""
This test will check if get_most_often is correctly returning the
correct value, which should be the item with the highest frequency
in our highest_items list
"""

def test_get_most_often_when_there_is_an_item_of_highest_frequency():
    most_often_object = MostOften(['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c'])
    assert most_often_object.get_most_often() == 'a'

""""
This test will check if get_most_often is correctly returning
the string 'no clear winner' if we have two items of equal frequency
in our self.starting_list
"""

def test_get_most_often_when_two_items_of_equal_frequency():
    most_often_object = MostOften(['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c'])
    assert most_often_object.get_most_often() == "no clear winner"