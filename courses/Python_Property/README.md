## Python's property(): Add Managed Attributes to Your Classes

With Python’s [`property()`](https://docs.python.org/3/library/functions.html#property), you can create **managed attributes** in your classes. You can use managed attributes when you need to modify an attribute’s internal implementation and don’t want to change the class’s public [API](https://en.wikipedia.org/wiki/API). Providing stable APIs will prevent you from breaking your users’ code when they rely on *your code*.

**Properties** are arguably the most popular way to create managed attributes quickly and in the purest [Pythonic](https://realpython.com/learning-paths/writing-pythonic-code/) style.

**In this tutorial, you’ll learn how to:**

- Create **managed attributes** or **properties** in your classes

- Perform **lazy attribute evaluation** and provide **computed attributes**

- Make your classes Pythonic using properties instead of **setter** and **getter** methods

- Create **read-only** and **read-write** properties

- Create consistent and **backward-compatible APIs** for your classes

You’ll also write practical examples that use `property()` for validating input data, computing attribute values dynamically, logging your code, and more. To get the most out of this tutorial, you should know the basics of [object-oriented programming](https://realpython.com/python3-object-oriented-programming/), [classes](https://realpython.com/python-classes/), and [decorators](https://realpython.com/primer-on-python-decorators/) in Python.
