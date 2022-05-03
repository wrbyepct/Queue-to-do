
"""
Length 1
"""
start_num_0 = 35
line_len_0 = 1

"""
Extreme length
"""
start_num_777 = 1
line_len_777 = 100000

"""
Even number start, even length
"""
start_num_1 = 30
line_len_1 = 4

start_num_5 = 30
line_len_5 = 6

"""
Even number start, odd length
"""
start_num_2 = 30
line_len_2 = 5

start_num_6 = 30
line_len_6 = 7

start_num_9 = 30
line_len_9 = 9

"""
Odd number start, even length
"""

start_num_3 = 31
line_len_3 = 4

start_num_7 = 31
line_len_7 = 6

start_num_10 = 31
line_len_10 = 8

"""
Odd number start, odd length
"""
start_num_4 = 31
line_len_4 = 5

start_num_8 = 31
line_len_8 = 7

start_num_12 = 31
line_len_12 = 9


def solution(start, length):
    """
    **** There is a way to know exactly what the checksum per row is
    **** All because the numbers are continuous in each row
    """
    # Patterns:
    # 1. If the start number is even:
    #     A. Then every four numbers is a zero
    #     B. If the number of the row % 4 is 3, then the result -> last number in the row + 1
    #     C. If the number of the row % 4 is 2, then the result -> 1
    #     D. If the number of the row % 4 is 1, then the result -> the last number in the row

    # 2. If the start number is odd:
    #        We can just ignore the first number, and follow the principles above
    #            and then XOR the first number with result above
    checksum = 0
    for row_length in range(length, 0, -1):
        checksum ^= get_checksum_per_row(start, row_length)
        start += length

    return checksum


def is_odd(n):
    return n % 2 != 0


def get_simplified_xor(start, length):
    if length % 4 == 3:
        # it's equivalent to the last number + 1
        return start + length

    if length % 4 == 2:
        # it's equivalent to 1
        return 1

    if length % 4 == 1:
        # it's equivalent to the last number
        return start + length - 1

    # if length % 4 == 0, it's equivalent to 0
    return 0


def get_checksum_per_row(start, length):
    if is_odd(start):
        # Calculate as if this is an "even number" start row
        return start ^ get_simplified_xor(start + 1, length - 1)

    return get_simplified_xor(start, length)


print(solution(start_num_1, line_len_1))
print(solution(start_num_5, line_len_5))
print(solution(start_num_7, line_len_7))

# Extreme cases
print(solution(start_num_0, line_len_0))
print(solution(start_num_777, line_len_777))



