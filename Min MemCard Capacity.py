def minimum_mem_cap(appmem,k):
    n = len(appmem)
    if n > k*2:
        return 0
    if k>= n:
        return max(appmem)
    else:
        appmem.sort(reverse=True)
        capacities = [max(appmem)]
        for i in range(n-1):
            for j in range(i+1,n):
                psum = appmem[i] + appmem[j]
                if psum > max(appmem) and psum not in capacities:
                    capacities.append(psum)
        
        capacities.sort()
        print("Possible Capacities = ",capacities)
        
        for capacity in capacities:
            feasible= 0
            i = 0
            j = n-1
            teams = 0
            while(i<=j and teams<=k):
                if i==j:
                    if teams < k:
                        feasible= 1
                    break
                if j == i+1 and teams<k:
                    if appmem[j]+appmem[i] <= capacity and teams+1 <= k:
                        feasible= 1
                    elif teams+2 <= k:
                        feasible= 1
                    break
                    
                if appmem[i] + appmem[j] <= capacity:
                    teams += 1
                    i+= 1
                    j-=1
                else:
                    teams += 1
                    i += 1
            if feasible == 1:
                return capacity
        
        return 0
            
        

if __name__ == "__main__":
    appmem = list(map(int,input("Enter app memories: ").split()))
    k = int(input("Enter no of teams: "))
    res = minimum_mem_cap(appmem,k)
    if res!=0:
        print(f"minimum memory card capacity needed so every team can download atmost 2 apps = {res}")
    else:
        print("Not possible")

#appmem = 10 6 7 12 1
#k = 3
#res = 13