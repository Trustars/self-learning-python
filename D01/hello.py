# -*- coding: utf-8 -*-

#print "hello" + " " + "world" + str(1)

#print "hello" + " " + "world" + str(2)


# counter = 1
# while counter <= 100:
#     print "hello" + " " + "world " + str(counter)
#     counter = counter + 1
#
# if True:
#     #do that
# else:
#     #do that instead

def max(arg1, arg2):
    """
        :return: the max of two number
    """
    # return arg1 if arg1 > arg2 else arg2
    if arg1 > arg2:
        return arg1
    else:
        return arg2

def max_of_three(arg1, arg2, arg3):
    """
        :return: the max of three number
    """
    # max_arg12 = max(arg1, arg2)
    # return max(max_arg12, arg3)
    return max(max(arg1, arg2), arg3)

result = max(1, 6)
print(result)
