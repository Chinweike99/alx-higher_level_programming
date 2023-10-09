#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    m_list = []
    if my_list:
        for num in my_list:
            m_list.append(False if num % 2 else True)
        return m_list
