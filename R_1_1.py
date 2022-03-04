
def is_multiple(n, m):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.1"""
    if m != 0: # no divison by zero

        if n % m == 0:
            return True
        else:
            return False
    else:
        print("We don't divide by zero! Enter another m!")

def is_even(k):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.2"""
    if k > 0: # for positive integers
        while k > 0:
            k -= 2
            if k == 0:
                return True
            elif k < 0:
                return False
    elif k < 0: #for negative integers
        while k < 0:
            k += 2
            if k == 0:
                return True
            elif k > 0:
                return False
    else: #for zero
        return True

def minmax(data):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.3"""
    n = len(data)
    if n == 1: #for single number
        return data[0], data[0]
    else:
        sorted_data = sorted(data)
        return sorted_data[0], sorted_data[n-1]
    
def squares(n):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.4"""
    if n > 0:
        sum = 0
        while n > 0:
            sum += (n-1)*(n-1) #add the squared previos integer to the sum
            n -= 1
        return sum
    else:
        return print('n must be positive!')

def single_line_squares(n):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.5"""
    squares = sum([integer**2 for integer in range(0, n) if n > 0])
    return squares

def odd_squares(n):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.6"""
    if n > 0:
        squares = 0
        while n > 0:
            #print(n-1)
            if (n-1) % 2 == 1:
                squares += (n-1)*(n-1)
                #print(squares)
                n -= 1
            else:
                squares = squares
                n -= 1
        return squares
    else:
        return print('n must be positive!')

def single_line_odd_squares(n):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.7"""
    odd_squares = sum([odd_integer**2 for odd_integer in range(0, n) if odd_integer % 2 != 0 and n > 0])
    return odd_squares

def list_copmreh(n):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.11"""
    powers_of_two = [2**power for power in range(0, n)]
    return powers_of_two

def choice_implementation(data):
    """M.T. Goodrich Data Structures and Algorithms, p. 51, Exercise R-1.12"""
    import random
    n = len(data)
    sorted_data = sorted(data)
    least, greatest = sorted_data[0], sorted_data[n-1]

    choice = random.randrange(least, greatest+1)

    while True:
        if choice in data:
            return choice
        else:
            choice = random.randrange(least, greatest+1)

def produce_list(n):
    """M.T. Goodrich Data Structures and Algorithms, p. 52, Exercise C-1.18"""
    produced_list = [(i*(i+1)) for i in range(0, n-1)]
    return produced_list

def dot_product(a, b):
    """M.T. Goodrich Data Structures and Algorithms, p. 53, Exercise C-1.22"""
    if len(a) == len(b):
        c = [a[i]*b[i] for i in range(0, len(a))]
        return c
    else:
        print('arrays a and b have different lengths')

