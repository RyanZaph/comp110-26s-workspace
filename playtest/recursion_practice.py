def add_one(num):

    if num >= 9:
        return num + 1

    total = num + 1  # only if num is less than 9
    print(total)  # recursive call to the function

    return add_one(total)


my_new_total = add_one(0)  # this is the number and it goes to the next one over
print(my_new_total)
