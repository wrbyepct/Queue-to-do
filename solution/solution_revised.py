
"""
Informal Structured Outline



Problem type:
    Pattern Detecting

The gist of the problem:
    XOR the continuous integers within restricted rules


Input range:
    0 ≤ ID size ≤ 2000000000
    Decreasing length ≥ 1


Concerned target:
    Continuous XOR pattern

Goal:
    Calculate the XOR sum correctly and fast


What we have known:
    1. If the number line starts with an even number, then the XOR sum of every 4 continuous numbers are zero
        E.g.
            4 ^ 5 ^ 6 ^ 7 => 100 ^ 101 ^ 110 ^ 111
    2. If the number is even, then the XOR of it's next is ALWAYS 1
        E.g.
            4 ^ 5 => 100 ^ 101 = 1
            6 ^ 6 => 110 ^ 111 = 1
    3. If the number is even, then the XOR of it with 1 is the number plus 1
        E.g.
            1 ^ 4 => 001 ^ 100 = 101 = 5
            1 ^ 6 => 001 ^ 110 = 111 = 7


Conclusion:
    1. If the number line start with even number, then next we just need to know if the length is divisible by 4
            If not, then we always know it's just a game with 3, 2, or 1 last remaining numbers
            E.g.
                number line = 4, 5, 6, 7, 8, 9, 10
                length = 7
                remainder = 3
                It's a game of 8, 9, 10, which is even, odd, even.
                even ^ odd is 1 (1000 ^ 1001 = 1) , 1 ^ even is its next(0001 ^ 1010 = 1011 = 11 )
                which is 11
    2. If the number line start with odd number, then we can just simply remove the first number
        and follow the same principle to calculate the result, and then XOR with the start


Must do in order to achieve the goal:
    1. Imagine we are calculating every line, and then sum them together
        So in forloop each run is to calculate the sum of one number line
    2. There 4 cases with has to be dealt with:
        number length remainder = 0 -> 0,
                                  1 -> the last number in the line
                                  2 -> 1
                                  3 -> the last number in the line + 1
    3. If the start number is odd, remove it first and treat the line like it starts with even
        remember to subtract the length with 1

===============================================================

Formal Description

-------------Definitions--------------
start: Int
checkLength: Int
checkSum: Int
lineChecksum(start, l, r):
    result := -1
    { (r = 0 ∨ r = 1 ∨ r = 2 ∨ r = 3) ∧ result = -1 }
    IF
        r = 0 -> result := 0
        r = 1 -> result := start + l - 1
        r = 2 -> result := 1
        r = 3 -> result := start + l
    FI
    { result ≠ -1 }

---------------Steps-------------------
l := checkLength;
n := l;
checkSum := 0;

{ 1 ≤ n ≤ 2000000000 ∧ l ≥ 1 ∧ checkSum = { XOR i | 0 ≤ i < n: lineCheckSum(start + i*l, n - i)} }
DO n > 0
    IF
        isEven(start) ->
            remainder := l % 4;
            checkSum := checkSum XOR lineChecksum(start, n, remainder)
        isOdd(start) ->
            remainder := (l - 1) % 4;
            checksum := checkSum XOR start XOR lineChecksum(start + 1, n - 1, remainder)
    FI;
    start := start + l;
    n := n - 1
OD
{ n = 0 ∧ l ≥ 1 ∧ checkSum = { XOR i | 0 ≤ i < n: lineCheckSum(start + i*l, n - i)} }

"""

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