import json
from os import path as path_lib

class Test_Error(BaseException):
        pass

def check_test(l):
    if False in l: 
        raise Test_Error

def example_1_fib():
    """
    this is a docstring it explaines what the function does
    doc strings are very important, however the code you write should be easily 
    interpretable. 

    This function will generate the first 20 fibonacci numbers and record the history in a list.
    """
    fibonacci_history: list = [1] # list or array
    fibonacci_seqence: int = 1 # single value

    for i in range(20):
        # increase the array size by 1 and add fibonacci sequence value to the last locations
        # see python docs - https://docs.python.org/3/tutorial/datastructures.html
        fibonacci_history.append(fibonacci_seqence)

        # fibonacci = current value + second last value from fibonacci history
        # see negative indcies - https://stackoverflow.com/questions/11367902/negative-list-index
        fibonacci_seqence = fibonacci_seqence + fibonacci_history[-2]

    print(fibonacci_history)
    return fibonacci_history

    

def example_2_datatypes():
    """
    here are the most common datatypes that are used
    lists can have mixed types like an int and a string
    """
    integer: int = 0
    string: str = 'hello world'
    decimal: float = 0.55
    a_list:list = [0,1,2]
    a_tuple: tuple = (0,1,2)
    a_list_of_lists: list = [['hi','hi'],['hi','hi']]
    a_list_of_tuples: list = [(0,1),(2,3)]
    a_set = {0,1,2}
    a_dictionary = {'key':'value','apple':'green','cherry':'red',0:'number 1'}

def example_3_iterators():
    """
    iterators to do tedious tasks in a sustainable way i.e automation
    lets access some elements in the list fruits
    """
    fruits = ['apples','pears','oranges']

    # range is the simplest integer looping mechanism
    for i in range(3):
        # we can access an element in fruits by indexing it with i
        fruit = fruits[i]

    # enumerate uses a generator or list and iterates over it we 
    # can access an element in order by using the variable fruit
    # with enumerate you can also access i which in some cases is very handy
    # it is also quicker than range
    for i,fruit in enumerate(fruits):
        pass

    # the fastest and most pythonic way to access elements inside of fruits is <for x in y>
    # is is the cleanest code... but you dont get the index position.
    for fruit in fruits:
        pass

    # this loop will be condinue indefinatly.... or until the break clause is called
    counter = 0

    while True:
        # lets add 1 to the counter everytime it loops
        counter += 1

        # now lets check when counter equals 10
        if counter == 10:
            #leave the while loop, works for any loop
            break 
        
        
def example_4_classes():
    """
    classes are like manufacturing lines
    you can create multiple similar objects that are related.
    """
    class animal:
        """
        I am an animal
        """
        def __init__(self,name,weight,age):
            self.name = name
            self.weight = weight # kg
            self.age = age # years


    tiger = animal('orange menace',160,10)
    seal = animal(name='chonk',weight=50,age=17)

    tiger.weight # will result in 160
    seal.name # will result in 'chonk'



def test_1():
    """
    fill the function
    load json
    read - https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
    
    """
    #relative path works anywhere
    json_path = path_lib.join(path_lib.abspath(__file__),'..\\task1.json')

    magic_word = None
    return magic_word

def test_2():
    """
    now you can read a file we will do it again with another popuar filetype 
    cool --> csv's <-- cool 
    they are good for storing numbers :)
    but we will be searching for words ... a wordsearch

    """
    path_to_wordsearch = path_lib.join(path_lib.abspath(__file__),'..\\wordsearch.csv')

    # find the position in the array that equals the semi-colon there is only 1
    # i.e  word_search[x][y] = magic word, find x,y
    x = None
    y = None
    return x,y

def test_3():
    """
    regex and string manipulation
    regex cheat sheet - https://regexcheatsheet.com/
    use regex and string manipulation to retrive various parts of the string
    and supply the index
    so for fox and index of f the first letter of what your finding
    (fox,17),(<word>,<index>),...
    regex_1 find 'quick' and suppy index
    regex_2 find the 2nd 'the'
    regex_3 find the letter after u if the letter before is not q
    sm_1 reverse the string
    sm_2 slice the word dog off the string
    """
    test_string = 'the quick bro/wn fox jumpe/d over the lazy dog'
    regex_1 = r'' 
    regex_2 = r'' 
    regex_3 = r''
    sm_1 = ''
    sm_2 = ''
    return None

def test_4(numbers_to_test: list):
    """
    using api's to retrive something from a server
    the endpoint is https://api.isevenapi.xyz/api/
    look at example api response for an example url

    in the parameters you will see 'numbers_to_test'

    you will iterate over the list using a for loop
    and create a new list that contains boolean data 
    whether the number is even you have to use the api 
    to assess whether the number is even 

    you will need a libaray to complete this task

    e.g
    numbers_to_test = [1,2,3,4]
    is_even = [False,True,False,True]
    """
    is_even = None
    return is_even

def test_5():
    """
    classes 
    first create a constructor - look at google if you dont know
    after there should be an attribute called name and the constructor shouold set this name
    after a method should be added called generate_name and should have a parameter called name_options
    this function will return a randomly selected name from the list 
    """
    names = ['bob','jerry','sid']
    class nameless():
        pass

    return nameless()

def test_6():
    """
    benchmarking and iterators
    now we will test some number functions for the speed of computation
    take a look at https://stackoverflow.com/questions/25785243/understanding-time-perf-counter-and-time-process-time
    you will need the time library for this
    find all the times and return the lowest time as a number in one hot form


    e.g if the answer is n1
    funcs =                 [n0,n1,n2,n3,n4,n5]
    fastest_func_one_hot =   [0, 1, 0, 0, 0, 0]

    extra: find a new method which is faster than all examples
    """
    from operator import add

    #start with this list 
    #add 2 to all elements  in 5 different ways then eval uate the fastest
    numbers = [i for i in range(1000)]

    # use map and a lambda function
    n0 = None

    # change each element in the array by +2 (for loop)
    n1 = None

    # same thing but using list comprehension
    n2 = None

    # use map and add for this you need 2 lists
    n3 = None

    # use zip and sum with 2 lists
    n4 = None

    # extra
    n5 = None

    fastest_func_one_hot = [0,1,0,0,0] #change me
    return fastest_func_one_hot



def test_7():
    """
    unit testing
    we wont be looking at unittest or pytest modules,
    just covering the concepts to developing better code 
    to test 1 we can do somthing like 

    test = test_1() == expected_answer

    there are end to end, integration, unit and functional tests
    what we are doing here is unit testing
    the value of testing increasing as the amount of people writing the code base and the size of the code base increases

    the point of unit tests is to ensure a single function is behaving as expected 
    then we know when debugging that a function is at least completeing the tasks that the test laid out
    if you wrote the test wrong your assumptions about the test will be wrong

    we are going to make some tests for your previous code 

    I will do test 6 as an example and you need to complete test 4 
    more reading - https://www.atlassian.com/continuous-delivery/software-testing/types-of-software-testing#:~:text=The%20different%20types%20of%20tests%201%20Unit%20tests.,in%20a%20complete%20application%20environment.%20More%20items...%20

    """
    
    # example test_6
    result = test_6()
    expected_result = [0,1,0,0,0] # not the right answer :) change me when you know the answer

    # assumptions
    # result is a list
    # in said list there are only 0's nad 1's
    # there is only one 1 
    t6_0 = type(result) is list

    # a set is unordered but there can only be a single value of each item so {1,1} is not a set {1} is
    # we are testing the result when converted to a set which should be {1} {0} {0,1} is a subset of {0,1}
    t6_1 = set(result).issubset({0,1}) 

    # create a dictionary which stores key:value pairs
    # key being each result so 0,1 and the value being the freuency
    # update updates the dictionary with a new key:value pair it can overwrite
    # so we update the old key:value pair with a new key:value+1 pair
    # for every element in result
    freq = {}
    for i in result:
        freq[i] = freq.get(i,0) + 1

    t6_2 = freq[1] == 1

    #check the statements are true
    check_test([t6_0,t6_1,t6_2])


    # unit test for test_4
    check_test([])


    t4_0 = None
    return 
    






def run_test():
    return test_1(),test_2(),test_3(),test_4([1,56,79,10,32]),test_5(),test_6(),test_7()

if __name__ == "__main__":
    run_test()
