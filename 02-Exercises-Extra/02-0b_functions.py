# 1. Write a function that iterates through a list and prints each value without using a loop.
# That is, write a recursive function to print the values of a list.
listData = [1, 5, 6, 10, 15, 2, 44]

# "wrong" solution (using a loop, not allowed)


def iterListPrintValue():
    for num in listData:
        print(num)


print("'Wrong' solution: ")
iterListPrintValue();
print("'Right' solution:")
# "right" solution (using recursive function)


def recursive_print(lst):
    if not lst:
        print("Debug: I have been hit, I have no elements in my lst, most likely because lst.pop() removed it all, and my recursive call has been triggering several of times!")
        return

    # note: The pop() method returns the item present at the given index. This item is also removed from the list.
    print(lst.pop())

    # This is recursion I think. Recursion is when a function calls another copy of itself to finish the work
    recursive_print(lst)
    # It continues until lst.pop has removed everything from the list


recursive_print(listData);
print("* Exercise 2: *")  # [num for num in range (1, 20+1)
# Write a function that can take any number of arguments and return all arguments concatenated or summed depending on the data type

# could probably have been made better, coding wise :d
def recurv_print_two(*passedData):
       sum = 0
       strConc = ""
       
       for i in passedData:
           if type(i) == int or type(i) == float:
               sum += i
           elif type(i) == str:
               strConc += " " + str(i)
       if sum > 0: # then it's an integer
           return sum
       else: # then we consider it as a string
            return strConc
    
# should probably have some validation if one argument is a String, and the other is an int...
print(recurv_print_two("hello", "hello"))
print(recurv_print_two(200, 100))
