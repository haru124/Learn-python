import cook

cook.make_sandwich()


# This script imports the `cook` module and calls the `make_sandwich` function defined in it.
# This demonstrates how to use functions from another module while ensuring that the function is only executed when the script is run directly, not when imported.

'''In the cook.py file, the function `make_sandwich` is defined, and it prints "Sandwich made!" when called. The function make_sandwich is called inside `if __name__ == "__main__":` this means that the function will only execute when the cook.py file is run directly, not when it is imported as a module in another script.'''

'''
if __name__ == "__main__": is not used in cook.py file, that is if the make_sandwich function is directly called in the cook.py file, it will execute immediately when the module is imported.
# This is generally not recommended for functions that are meant to be used as part of a module, as it can lead to unintended side effects when the module is imported elsewhere.'''

'''Here the function make_sandwich is not called inside the if __name__ == "__main__": block, which means it will execute immediately when this script is run, regardless of whether it is imported as a module or run directly. This is generally not recommended for functions that are meant to be used as part of a module, as it can lead to unintended side effects when the module is imported elsewhere.'''