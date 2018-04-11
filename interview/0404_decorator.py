import os

print(os.path.isfile('0304_metaclass.py'))


#'''
def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped

def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
#@makeitalic
def hello():
    return "hello world"

print(hello()) ## returns "<b><i>hello world</i></b>"

'''
# A decorator is a function that expects ANOTHER function as parameter
def my_shiny_new_decorator(a_function_to_decorate):
    def the_wrapper_around_the_original_function():

        # Put here the code you want to be executed BEFORE the original function is called
        print("Before the function runs")

        # Call the function here (using parentheses)
        a_function_to_decorate()

        # Put here the code you want to be executed AFTER the original function is called
        print("After the function runs")

    # At this point, "a_function_to_decorate" HAS NEVER BEEN EXECUTED.
    # We return the wrapper function we have just created.
    # The wrapper contains the function and the code to execute before and after. It’s ready to use!
    return the_wrapper_around_the_original_function

# Now imagine you create a function you don't want to ever touch again.
#def a_stand_alone_function():
#    print("I am a stand alone function, don't you dare modify me")

#a_stand_alone_function()
#outputs: I am a stand alone function, don't you dare modify me

# Well, you can decorate it to extend its behavior.
# Just pass it to the decorator, it will wrap it dynamically in
# any code you want and return you a new function ready to be used:

#a_stand_alone_function_decorated = my_shiny_new_decorator(a_stand_alone_function)
#a_stand_alone_function_decorated()
#outputs:
#Before the function runs
#I am a stand alone function, don't you dare modify me
#After the function runs


@my_shiny_new_decorator
def another_stand_alone_function():
    print("Leave me alone")
another_stand_alone_function()



def bread(func):
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper():
        print("#tomatoes#")
        func()
        print("~salad~")
    return wrapper

def sandwich(food="--ham--"):
    print(food)



sandwich()
sandwich = bread(ingredients(sandwich))
sandwich()




@bread
@ingredients
def sandwich(food="--ham--"):
    print(food)
sandwich()
'

@ingredients
@bread
def strange_sandwich(food="--ham--"):
    print(food)

strange_sandwich()



def method_friendly_decorator(method_to_decorate):
    def wrapper(self, lie):
        lie = lie - 3
        return method_to_decorate(self, lie)
    return wrapper



class Lucy(object):

    def __init__(self):
        self.age = 32

    @method_friendly_decorator
    def sayYourAge(self, lie):
        print("I am %s, what did you think?" % (self.age + lie))

l = Lucy()
l.sayYourAge(-3)

'''

