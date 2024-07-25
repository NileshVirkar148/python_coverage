# app/greeter.py

def greet(name):
    if not name:
        return "Hello, Stranger!"
    elif name.lower() == "alice":
        return "Hello, Alice! Welcome back!"
    else:
        return f"Hello, {name}!"

def farewell(name):
    if not name:
        return "Goodbye, Stranger!"
    elif name.lower() == "bob":
        return "Goodbye, Bob! See you soon!"
    else:
        return f"Goodbye, {name}!"
