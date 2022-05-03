
"""
Length 1
"""
start_num_0 = 35
line_len_0 = 1

"""
Extreme length
"""
start_num_777 = 1
line_len_777 = 10001

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


def print_check_line(start, length):
    # ID_to_check = get_workIDs_to_be_checked(start, length)
    # return clever_XOR(ID_to_check, length)
    return get_workIDs_to_be_checked(start, length)


def clever_XOR(workIDs, length):
    height = length
    total_elem = (1 + height) * height / 2
    number_to_be_XOR = []

    if height == 1:
        return workIDs[0][0]

    # Even start
    if workIDs[0][0] % 2 == 0:
        # Even length
        if height % 2 == 0:
            number_to_be_XOR = even_start_even_len_method(workIDs, height)
        else:
            # Odd length
            number_to_be_XOR = even_start_odd_len_method(workIDs, height)

    # Odd start
    if workIDs[0][0] % 2 != 0:
        # Even length
        if height % 2 == 0:
            number_to_be_XOR = odd_start_even_len_method(workIDs, height)

        else:
            number_to_be_XOR = odd_start_odd_len_method(workIDs, height)

    # Count how many 1s
    excluded = len(number_to_be_XOR)
    total_ones = (total_elem - excluded) / 2

    # Append 1 to XOR list if the total 1 size is not even
    if total_ones % 2 != 0:
        number_to_be_XOR.append(1)
    print(number_to_be_XOR)
    return checksum(number_to_be_XOR)


def odd_start_odd_len_method(workIDs, height):
    n_list = [workIDs[0][0]]
    # Even index, collect the first
    # Odd index, collect none
    for i in range(2, height, 2):
        n_list.append(workIDs[i][0])
    return n_list


def odd_start_even_len_method(workIDs, height):
    n_list = [workIDs[0][0], workIDs[height - 1][0]]
    # Even index, collect the first and the last
    # Odd index, collect the first
    even_index = True
    for i in range(2, height - 1):
        if even_index:
            n_list += [workIDs[i][0], workIDs[i][-1]]
        else:
            n_list.append(workIDs[i][0])
        # Toggle
        even_index = not even_index
    return n_list


def even_start_odd_len_method(workIDs, height):
    n_list = [workIDs[1][-1]]
    even_index = True
    # Even index row, collect the last one
    # Odd index row, collect the first and the last one
    for i in range(2, height):
        if even_index:
            n_list.append(workIDs[i][-1])
        else:
            n_list += [workIDs[i][0], workIDs[i][-1]]

        # Toggle
        even_index = not even_index

    return n_list


def even_start_even_len_method(workIDs, height):
    num_list = []
    for i in range(1, height, 2):
        num_list.append(workIDs[i][-1])
    return num_list


def checksum(to_be_XOR):
    final = 0
    for n in to_be_XOR:
        final ^= n
    return final


def get_workIDs_to_be_checked(start, length):
    line_distance = length
    workIDs = []
    while length > 0:
        ID_line = []
        for i in range(length):
            ID_line.append(start + i)

        length -= 1
        start += line_distance
        workIDs.append(ID_line)
    return workIDs


def brute_force_XOR(workIDs):
    checksum = 0
    for row in workIDs:
        for col in row:
            checksum ^= col
    return checksum


"""
Even start, even length
"""

workIDs_1 = print_check_line(start_num_1, line_len_1)
print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_1)}")

workIDs_5 = print_check_line(start_num_5, line_len_5)
print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_5)}")

workIDs_7 = print_check_line(start_num_7, line_len_7)
print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_7)}")


# print("")
# workIDs_5 = print_check_line(start_num_5, line_len_5)
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_5)}")
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_5, line_len_5)}")
#
# """
# Even start, odd length
# """
#
# print("\nThis is even number start, odd length: ")
# workIDs_2 = print_check_line(start_num_2, line_len_2)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_2, line_len_2)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_2)}")
#
# print("")
# workIDs_6 = print_check_line(start_num_6, line_len_6)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_6, line_len_6)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_6)}")
# print("")
# workIDs_9 = print_check_line(start_num_9, line_len_9)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_9, line_len_9)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_9)}")
#
# """
# Odd start, even length
# """
#
# print("\nThis is odd number start, even length: ")
# workIDs_3 = print_check_line(start_num_3, line_len_3)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_3, line_len_3)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_3)}")
#
# print("")
# workIDs_7 = print_check_line(start_num_7, line_len_7)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_7, line_len_7)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_7)}")
#
# print("")
# workIDs_10 = print_check_line(start_num_10, line_len_10)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_10, line_len_10)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_10)}")
#
# """
# Odd start, odd length
# """
#
# print("\nThis is odd number start, odd length: ")
# workIDs_4 = print_check_line(start_num_4, line_len_4)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_4, line_len_4)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_4)}")
# print("")
# workIDs_8 = print_check_line(start_num_8, line_len_8)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_8, line_len_8)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_8)}")
# print("")
# workIDs_12 = print_check_line(start_num_12, line_len_12)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_12, line_len_12)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_12)}")
#
#
# """
# Length 1
# """
# print("\nThis is random number start, 1 length: ")
# workIDs_0 = print_check_line(start_num_0, line_len_0)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_0, line_len_0)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_0)}")
#
# """
# Extreme length
# """
# print("\nThis is random number start, enormous length: ")
# workIDs_777 = print_check_line(start_num_777, line_len_777)
# print(f"This is the XOR sum(clever force): {clever_XOR(workIDs_777, line_len_777)}")
# print(f"This is the XOR sum(brute force): {brute_force_XOR(workIDs_777)}")
