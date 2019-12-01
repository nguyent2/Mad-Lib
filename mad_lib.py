#################################################################################
# Author: Jacob Barnwell, Jennifer Fidelia, Thy Nguyen
# Username: barnwellj, fideliaj, nguyent2
#
# Assignment: T09
# Purpose: To practice with using strings
#################################################################################
# Acknowledgements:https://www.woojr.com/halloween-mad-libs/scary-halloween-mad-lib/

#################################################################################


def function_1(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o):
    """
    Prints the madlibs story
    :param a,b,c,d,e,f,g,h,i,j,k,l,m,n,o
    :return none
    """
    story = """
    They say my school is haunted; my {0} friend {1} says she saw a {2} {3} floating at the end of the hall near the 
    cafeteria. Some say if you {4} down that hallway at night, you'll hear a {5} {6} {7}. My {8} friend {9} saw
    a {10} {11} {12} under one of the tables once. I hope I never see any {13} {14} ; 
    eating lunch there is scary enough!!
    """
    print(story.format(a, b, c, d, e, f, g, h, i, j, k, l, m , n, o))


def function_2():
    """
    Defining the variables and ask for user's input
    :param no parameter
    :return a,b,c,d,e,f,g,h,i,j,k,l,m,n,o
    """
    a = input("Enter an adjective")
    c = input("Enter an adjective")
    i = input("Enter an adjective")
    k = input("Enter an adjective")

    b = input("please enter a name")
    j = input("please enter a name")

    d = input("please enter a noun")
    l = input("please enter a noun")
    n = input("please enter a noun")

    e = input("please enter a verb")

    f = input("please give an animal")

    g = input("please a verb ending ing")
    m = input("please a verb ending ing")
    o = input("please a verb ending ing")

    h = input("please enter an adverb")

    return a,b,c,d,e,f,g,h,i,j,k,l,m,n,o

# def list_function():
#     """
#     This is the function to capture all the user's input into a list.
#     :return: list of inputs
#     """
#     list_of_inputs = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o]
#     return print(list_of_inputs)

def main():
    """
    This is the main function. To call other functions
    :return: none
    """
    #print(function_2())
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o = function_2()     # Unpacking the tuples
    function_1(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o)        # Function call to function_1


main()
