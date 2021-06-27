from functools import lru_cache
#      1. Write a function to return a list of the first n numbers in the Fibonacci string.
def problem_1():
    def fibonacci(n, generated_list):
        if n==1:
            generated_list = [0]
            return generated_list
        elif n==2:
            generated_list = [0, 1]
            return generated_list
        else:
            aux = fibonacci(n-1, generated_list)
            suma = sum(aux[-2:])
            aux.append(suma)
            return aux
    generated_list = []
    print(fibonacci(900, generated_list))

def problem_1_v2():
    @lru_cache(maxsize = 1000)
    def fibonacci(input_value):
        if input_value == 1:
            return 1
        elif input_value == 2:
            return 1
        elif input_value > 2:
            return fibonacci(input_value -1) + fibonacci(input_value -2)

    lista = []
    for i in range(1, 201):
        #  print("fib({}) = ".format(i), fibonacci(i))
        lista.append(fibonacci(i))
    print(lista)

# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

def problem_2():
    def prime_numbers(list_1: list):
        x=[x for x in list_1 if len([y for y in range(2,x//2+1) if x % y==0])==0]
        return x
    print(prime_numbers([2, 6, 20, 69, 13, 11, 4, 10, 2]))

# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a)

def problem_3():
    def operations_on_lists(list_1: list, list_2: list):
        intersection = []                         #intersection
        for i in list_1:
            if i in list_2:
                intersection.append(i)
        union = []                                #union
        for i in list_1:
            union.append(i)
        for i in list_2:
            if i not in list_1:
                union.append(i)
        first_minus_second = []                   #a-b
        for i in list_1:
            if i not in list_2:
                first_minus_second.append(i)
        second_minus_first = []                   #b-a
        for i in list_2:
            if i not in list_1:
                second_minus_first.append(i)
        result = intersection, union, first_minus_second, second_minus_first
        return result
    print(operations_on_lists([1, 2, 3], [3, 4, 5]))
# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). 
# The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.


