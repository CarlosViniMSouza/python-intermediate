## Creating Dictionaries With Literals and dict() ##

likes = {
    "color": "blue", 
    "fruit": "apple", 
    "pet": "dog"
}

print(likes)

fruits = dict(apple=0.40, orange=0.35, banana=0.25)

print(fruits)

## Using for Loops to Populate Dictionaries ##

potentiation = {}

for integer in range(0, 10):
    potentiation[integer] = 2 ** integer

print(potentiation)
