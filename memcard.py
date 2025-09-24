from collections import defaultdict

def minimum_mem_cap(appmem, k):
    n = len(appmem)
    if n > k*2:   # more apps than slots
        return 0
    if k >= n:    # each app gets its own team
        return max(appmem)
    
    appmem.sort(reverse=True)
    
    # All possible candidate capacities
    capacities = [max(appmem)]
    for i in range(n-1):
        for j in range(i+1, n):
            psum = appmem[i] + appmem[j]
            if psum > capacities[0] and psum not in capacities:
                capacities.append(psum)
    capacities.sort()

    # Try each candidate capacity
    for cap in capacities:
        # Fresh dictionary for each trial
        dic = defaultdict(list)
        for i in range(k):
            dic[i] = [appmem[i]]
        
        flag = 1
        for i in range(k, n):
            placed = False
            for j in range(k):
                if len(dic[j]) < 2 and sum(dic[j]) + appmem[i] <= cap:
                    dic[j].append(appmem[i])
                    placed = True
                    break
            if not placed:   # app couldn't be assigned
                flag = 0
                break
        if flag:
            return cap
    
    return 0

if __name__ == "__main__":
    appmem = list(map(int, input("Enter app memories: ").split()))
    k = int(input("Enter no of teams: "))
    res = minimum_mem_cap(appmem, k)
    if res != 0:
        print(f"Minimum memory card capacity needed so every team can download at most 2 apps = {res}")
    else:
        print("Not possible")

# Example:
# Input: 10 6 7 12 1
# k = 3
# Output: 13