
def longestsubstring(a,b,c):
    sslen = 0
    for i in len(b):
        j=0
        if b[i]==a[j]:
            j++
            
            
    return ss

if __name__=="__main__":
    
    a = input("Enter string 1: ")
    b = input("Enter string 2: ")
    c = input("Enter string 3: ")
    #print(f"Before function call: a = {a} , b = {b} , c = {c}")                 
    res = longestsubstring(a,b,c)
    #print(f"After function call: a = {a} , b = {b} , c = {c}")
    print("Longest substring among a,b & c is ",res)