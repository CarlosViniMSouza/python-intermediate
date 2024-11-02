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

def make_calculator(root_degree, preicion=2):
    def root_calculator(number):
        return round(pow(number, 1 / root_degree), preicion)
    
    return root_calculator

square_root = make_calculator(2, 2)
print(f"The root of 50 is {square_root(50)}")
