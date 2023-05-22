#!/usr/bin/env python3
# # -*- coding: utf-8 -*-

def sum_after_negative(*args):
    found_negative = False
    total_sum = 0

    for arg in args:
        if found_negative:
            total_sum += abs(arg)
        elif arg < 0:
            found_negative = True

    return total_sum
if __name__ == "__main__":
    print(sum_after_negative(1, 2, 3, 0, 4, -5, 6))
    print(sum_after_negative(0, 5, -7, 9, -2))
    print(sum_after_negative(-2, 7, 0, 3, -8, -5, 0, 1))


