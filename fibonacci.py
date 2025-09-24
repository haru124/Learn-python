def fib(n):
    if n == 0:
        print(f"The Fibonacci of {n} is {int(0)}")
        return 0
    elif n == 1:
        print(f"The Fibonacci of {n} is {int(1)}")
        return 1
    else:
        print(f"The Fibonacci of {n} is {fib(n - 1) + fib(n - 2)}")    
        #These print statements will run for every recursive call causing error  - undesirable
        return fib(n - 1) + fib(n - 2)
          
    
def fib_memoization(n, fib={}):
    if n in fib:
        return fib[n]
    if n == 0:
        return 0
    elif n == 1:            
        return 1
    else:
        fib[n] = fib_memoization(n - 1, fib) + fib_memoization(n - 2, fib)
        return fib[n]

if __name__ == "__main__":
    # Input from user
    
    n = int(input("Enter n: "))
    #fib(n)
    fib = {}
    fib_memoization(n,fib)
    print("Fibonacci series up to", n, "is:", [fib[i] for i in range(n+1)])


"""
Example output for function fib(n):

    Enter n: 4
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 2 is 1
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 1 is 1
The Fibonacci of 3 is 2
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 2 is 1
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 1 is 1
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 2 is 1
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 4 is 3
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 2 is 1
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 1 is 1
The Fibonacci of 3 is 2
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 2 is 1
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 1 is 1
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0
The Fibonacci of 2 is 1
The Fibonacci of 1 is 1
The Fibonacci of 0 is 0

    # To avoid this, we can remove the print statements from here and only print the final result.
    ##This also shows that the recursive calls are made multiple times for the same value of n, leading to inefficiency. 
    To optimize this, we can use memoization or an iterative approach.
    """
            
            


    