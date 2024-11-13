## Inner Functions ##

"""
def hello_user():
    name = "Carlos"

    def print_message():
        print(f"Hello {name}")

    print_message()

hello_user()
"""

## Function Closures ## 

"""
def hello_user():
    name="Souza"

    def print_message():
        return f"Hello {name}"
    
    return print_message

hello = hello_user()
print(hello()) # output: Hello Souza

## Using Lambda ##

def hello_user():
    name="Carlos"
    return lambda: print(f"Hello {name}!")

hello = hello_user()
hello() # output: Hello Carlos!
"""

### Capture Variables ##

"""
def outer_func(outer_arg):
    def closure():
        print(outer_arg)
        print(local_var)
        print(another_local_var)

    local_var = "Outer local variable"
    another_local_var = "Another outer local variable"

    return closure

closure = outer_func("Outer argument")
closure() 
# output: Outer argument
# output: Outer local variable
# output: Another outer local variable
"""

"""
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

myCounter = make_counter()
result = myCounter() * 5

print(f"The variable counted {result} calls.") 
# output: The variable counted 5 calls.
"""

"""
def make_appender():
    items = [] # you don’t have to use the 'nonlocal'

    def appender(new_item):
        items.append(new_item)
        return items
    
    return appender

appender = make_appender()

print(appender("First item"))
# ['First item']

print(appender("Second item"))

# ['First item', 'Second item']
print(appender("Third item"))
# ['First item', 'Second item', 'Third item']
"""

## Creating Factory Functions ##

"""
def make_calculator(root_degree, preicion=2):
    def root_calculator(number):
        return round(pow(number, 1 / root_degree), preicion)
    
    return root_calculator

square_root = make_calculator(2, 2)
print(f"The root of 50 is {square_root(50)}")
"""

## Building Stateful Functions ## 

"""
def cumulative_average():
    data = []

    def average(value):
        data.append(value)
        return sum(data) / len(data)

    return average

stream_average = cumulative_average()

result = stream_average(10)
result = stream_average(12)
result = stream_average(6)

print(f"Stream Average Total: {result:.2f}") 
# output: Stream Average Total: 9.33
"""

## Providing Callback Functions ##

"""
import tkinter as tk

app = tk.Tk()
app.title("GUI App")
app.geometry("320x240")

label = tk.Label(
    app,
    font=("Helvetica", 16, "bold"),
)
label.pack()

def callback(text):
    def closure():
        label.config(text=text)

    return closure

button = tk.Button(
    app,
    text="Greet",
    command=callback("Hello, World!"),
)

button.pack()
app.mainloop()
"""

## Writing Decorators With Closures ##

"""
def decorator(function):
    def closure():
        print("\nDoing something BEFORE calling the function.")
        function()
        print("\nDoing something AFTER calling the function.")
    
    return closure

@decorator
def greet():
    print("Hi, Pythonista!")

greet()
"""

## Implementing Memoization With Closures ##

"""
from time import sleep
from timeit import timeit

def memoize(function):
    cache = {}

    def closure(number):
        if number not in cache:
            cache[number] = function(number)

        return cache[number]
    
    return closure

@memoize
def slow_operation(number):
    sleep(0.5)

print(timeit(
    "[slow_operation(number) for number in [2, 3, 4, 2, 3, 4]]",
    globals=globals(),
    number=1,
))
"""

## Achieving Encapsulation With Closures ##

"""
class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.pop()
stack.push(8)

print(stack._items)
"""

# Again, a closure provides a trick for achieving a stricter data encapsulation.

"""
def Stack():
    _items = []

    def push(item):
        _items.append(item)

    def pop():
        return _items.pop()

    def closure():
        pass

    closure.push = push
    closure.pop = pop

    return closure

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(4)
stack.pop()
stack.push(8)

print(stack.push.__closure__[0].cell_contents)
"""

## Exploring Alternatives to Closures ##

"""
def make_root_calculator(root_degree, precision=2):
    def root_calculator(number):
        return round(pow(number, 1 / root_degree), precision)

    return root_calculator

square_root = make_root_calculator(2, 4)
print(square_root(42)) # output: 6.4807

cubic_root = make_root_calculator(3)
print(cubic_root(42)) # output: 3.48
"""

"""
class RootCalculator:
    def __init__(self, root_degree, precision=2):
        self.root_degree = root_degree
        self.precision = precision

    def __call__(self, number):
        return round(pow(number, 1 / self.root_degree), self.precision)

square_root = RootCalculator(2, 4)
print(square_root(42)) # output: 6.4807

cubic_root = RootCalculator(3)
print(cubic_root(42)) # output: 3.48

print(cubic_root.root_degree) # output: 3
"""
