#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    my_list = []
    for i in range(list_length):
        try:
            j = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            j = 0
            print("wrong type")
        except IndexError:
            j = 0
            print("out of range")
        except ZeroDivisionError:
            j = 0
            print("division by 0")
        finally:
            my_list.append(j)
    return (my_list)
