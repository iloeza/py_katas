"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]

"""


def move_zeros(lst):
    return [number for number in lst if number != 0] + [zero for zero in lst if zero == 0]


move_zeros([1, 2, 1, 1, 0, 3, 0, 1, 0, 0])
