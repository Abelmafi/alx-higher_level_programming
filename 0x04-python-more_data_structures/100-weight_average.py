#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return (0)
    new_mul = [x[0]*x[1] for x in my_list]
    new_sum = [y[1] for y in my_list]
    sum_d = 0
    sum_s = 0
    for i in range(len(my_list)):
        sum_d += new_mul[i]
        sum_s += new_sum[i]
    avg = sum_d / sum_s
    return avg
