"""
Problem Statement

You are given a list of integers where each integer represents the memory requirement (in MB) to download an app. There are k teams, and each team is provided with one memory card.

The rules for assigning apps are as follows:

Each team must be able to download at least one app.
A team can download at most two apps.
All memory cards given to teams must have the same storage capacity.
Your goal is to minimize this storage capacity while ensuring all apps can be distributed among the teams.
Return the minimum memory card capacity required.

Example 1
Input: 
apps = [10, 6, 7, 12, 1]
k = 5
Output: 
12

Explanation:

Each team can take one app.
The maximum app size is 12, so a memory card of size 12 MB is sufficient.

Example 2
Input: 
apps = [10, 6, 7, 12, 1]
k = 3
Output: 
13

Explanation:

We must group the apps into 3 teams.
One possible grouping:
Team 1 → (12)
Team 2 → (10, 1)
Team 3 → (7, 6)

The maximum size among these groups is 13.
So, the minimum required card size is 13 MB.
"""
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