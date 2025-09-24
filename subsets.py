def generate_subsets(S):
    call_counter = 0

    """
    call_counter = [0]
    
    inside recursion function :
    call_counter[0]+= 1
    
    this is called Wrap state in a mutable container (list or dict)
    
    or inside a class as a variable 
    
   << can also use global variable >>
    """
    def backtrack(index, current_subset):
        nonlocal call_counter
        call_counter += 1
        print(f"Call {call_counter}: index={index}, current_subset={current_subset}")

        if index == len(S):
            results.append(current_subset[:])
            return

        current_subset.append(S[index])
        print(f"Appended S[{index}]={S[index]}, c_ss = {current_subset}")
        backtrack(index + 1, current_subset)
        current_subset.pop()
        print(f"Popped S[{index}]={S[index]}, c_ss = {current_subset}")
        backtrack(index + 1, current_subset)

    results = []
    backtrack(0, [])
    return results

ss = ['A','B','C','D']
res = generate_subsets(ss)
print(res)

"""
### Use a class with an instance variable ###

Encapsulate the recursion in an object:

class Solver:
    def __init__(self):
        self.call_counter = 0

    def backtrack(self, index, current_subset):
        self.call_counter += 1
        # recursion continues...
        
"""

"""
### Use a decorator (function wrapper)###

from functools import wraps

def count_calls(func):
    func.call_counter = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        func.call_counter += 1
        return func(*args, **kwargs)
    return wrapper

@count_calls
def backtrack(index, current_subset):
    # recursion
    if index < 3:
        backtrack(index+1, current_subset)

backtrack(0, [])
print(backtrack.call_counter)
"""