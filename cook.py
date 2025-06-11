#understanding the use of __name__ == "__main__"

def make_sandwich():
    print("Sandwich made!")

if __name__ == "__main__":
    make_sandwich()
    
'''The function is called inside the if block, which means it will only execute when this script is run directly, not when imported as a module. This is useful for testing or running code that should not execute when the module is imported elsewhere. 

To use this function in another script, you would import the module and call `cook.make_sandwich()` without triggering the execution of the function automatically. This is a common practice in Python to allow for both module functionality and standalone script execution.

If the function were called outside of the `if __name__ == "__main__":` block, it would execute immediately upon import, which is usually not desired behavior for functions that are meant to be used as part of a module.'''