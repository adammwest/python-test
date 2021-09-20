import os 

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


    tiger = animal('tiger',160,10)
    seal = animal('seal',50,17)



def test_1():
    """
    fill the function
    load json
    read - https://www.geeksforgeeks.org/how-to-read-from-a-file-in-python/
    
    """

    # line of code to read a file
        # print both key value pairs of the json object
    magic_word = None # change to read value in json
    return magic_word

def test_2():
    """
    now you can read a file we will do it again with another popuar filetype 
    cool --> csv's <-- cool 
    they are good for storing numbers :)
    but we will be searching for words ... a wordsearch

    """
    path_to_wordsearch = ""
    # load the document words.csv
    # make a 2d  list
    word_search = [[]]

    # find the position in the array that equals the magic word
    # i.e  word_search[x][y] = magic word, find x,y
    x = None
    y = None
    return x,y

def test_3():
    """
    regex and string manipulation
    """
    return None

def test_4():
    pass

    



def unit_test():
    """
    """



def run_tests():
    example_1_fib()
    example_2_datatypes()
    example_3_iterators()
    example_4_classes()

    test_1()




if __name__ == "__main__":
    run_tests()