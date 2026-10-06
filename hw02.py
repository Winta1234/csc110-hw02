# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    """ takes two integer inputs and return them as x, y"""
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x= int(input("give me x: "))# to ask for input for the first number
    y= int(input("give me y: "))
    return x,y


# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    # ADD a Docstring for this function
    """ Take two integer inbut and return the ratio of their multipliction to their addition"""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    mult_result = a * b # multiply the firt number to the second  one
    print(f"mult result: {mult_result}")
    add_result = a + b # to add the first number to the second one
    print(f"add result: {add_result}")
    return mult_result / add_result
# xy_multadd= compute_multadd(a,b)
    

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    # ADD a Docstring for this function
    """ print diffrent things that are inputed in the previous functions"""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    first_string= "*"*16 # create 16 * and assign it to a variable
    print(first_string)
    print("RESULTS:")
    print(f"first number: {a}")
    print(f"second number: {b}")
    print(f"multadd result: {ab_multadd}")
    second_string= "="*16
    print(second_string)# create 16 = and assign it to a variable
    
def main ():
    # ADD a Docstring for this function
    """main function to call all the function we defined"""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y
#     read_two_ints()
    x, y = read_two_ints()
    
    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    xy_multadd = compute_multadd(x,y)
    
    
    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
