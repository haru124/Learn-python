def calcwork(h):
    """Calculate the minimum work required to balance wine bottles among houses.
    :param h: List of integers representing the number of wine bottles each house holds or needs.
    :return: Integer representing the minimum work required.
    """
    work = 0
    n = len(h)
    for i in range(n):
        while h[i] !=0 :
            for j in range(i+1,n) :
                if h[i] > 0:
                    if h[j] < 0:
                        break
                elif h[i] < 0:
                    if h[j] > 0:
                        break
            print(f"i = {i},j = {j}")
            dis = j-i
            m = min(abs(h[i]), abs(h[j]))
            work += dis*m
            if h[i] > 0 :
                h[i] -= m
                h[j] += m
            elif h[i] < 0 :
                h[i] += m
                h[j] -= m
        
            print("Bottles = ",h)
            print("Work = ", work)
    
    return work

def optimized_calcwork(h):

    work = 0
    cumulative = 0
    for i in range(len(h)):
        cumulative += h[i]
        work += abs(cumulative)
        print(f"House {i}: Bottles = {h[i]}, Cumulative = {cumulative}, Work = {work}")
    return work

if __name__ == "__main__":
    
    h = list(map(int,input("Enter no of wine bottles each house holds/needs\n").strip().split()))
    print("No of wine bottles each house holds/needs: ",h)
    work = calcwork(h)
    print("Minimum work required to balance wine bottles: ", work)
