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

# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).

def problem_5():
    def set_zero_under_diagonal(matrix):
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                if i > j:
                    matrix[i][j] = 0
        return matrix
    matrix = [ [1 for i  in range(5) ] for j in range(5)]

    #printing the matrix
    set_zero_under_diagonal(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            print(matrix[i][j], end="")
        print()

#  6. Write a function that receives as a parameter a variable number of lists and a whole number x.
#  Return a list containing the items that appear exactly x times in the incoming lists
# TODO: do this again after you learn what a dictionary is and how it works
def problem_6():
    def count_items(x, *args):
        frequency_of_values = []
        found_values = []
        for found_list in args:
            if isinstance(found_list, list):
                for value in found_list:
                    if value not in found_values:
                        found_values.append(value)
                        frequency_of_values.append(1)
                    else:
                         index = found_values.index(value)
                         frequency_of_values[index] = frequency_of_values[index] + 1
        print("all the unique values in the lists are: ", found_values)
        print("their frequency index is: ", frequency_of_values)

        result = []
        for i in range(0, len(frequency_of_values)):
            if frequency_of_values[i]==x:
                result.append(found_values[i])
        return result
    print(count_items(2, [4, 5, 6, 1024012, 2, 50, 1, 1, 69, "test"], [4, 5, "test", 69]))


# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements. 
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be the greatest palindrome number.
def problem_7():                   
    def palindrome_counter(number_list):
        def palindrome_check(number):
            number = str(number)
            for index in range(0, len(number)//2):
                if number[index]!=number[-1-index]:
                    return False
            return True
        number_of_palindromes = 0
        greatest_palindrome = 0
        for number in number_list:
            if palindrome_check(number):
                number_of_palindromes += 1
                if number > greatest_palindrome:
                    greatest_palindrome = number
        return (number_of_palindromes, greatest_palindrome)
    print(palindrome_counter([10, 121, -121, 20, 66, 606]))

#  8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
#  For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
#  otherwise it should contain characters that have the ASCII code not divisible by x.

def problem_8():
    def ascii_divisor(x = 1, list=[] , flag=True):
        result_list = []
        for word in list:
            word_index = list.index(word)
            result = []
            for char_index in range(0, len(word)):
                if (ord(word[char_index]) % x)==0 and flag == True:
                    print("found character", word[char_index], "which is not divisible by", x)
                    result.append(word[char_index])
                if (ord(word[char_index]) % x)!=0 and flag == False:
                    print("found character", word[char_index], "which is divisible by", x)
                    result.append(word[char_index])
            result_list.append(result)
        return result_list
    print(ascii_divisor(2, ["test", "hello", "lab002"], False))
problem_8()




