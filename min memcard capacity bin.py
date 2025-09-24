#-- not correct --
"""
def minimum_mem_cap(appmem, k):
    n = len(appmem)
    
    # If more apps than 2*k slots, not possible
    if n > 2 * k:
        return -1  
    
    appmem.sort()  # sort ascending
    
    def canDistribute(capacity):
        '''Check if all apps can be assigned within k teams given capacity.'''
        i, j = 0, n - 1
        teams = 0
        while i <= j:
            if i == j:  # one app left
                teams += 1
                break
            if appmem[i] + appmem[j] <= capacity:  # fit two apps
                i += 1
                j -= 1
            else:  # only take the bigger app
                j -= 1
            teams += 1
            if teams > k:
                return False
        return True
    
    # Binary search range
    left, right = max(appmem), appmem[-1] + appmem[-2]  # max single app to sum of 2 largest
    
    res = -1
    while left <= right:
        mid = (left + right) // 2
        if canDistribute(mid):
            res = mid
            right = mid - 1  # try smaller
        else:
            left = mid + 1  # need bigger capacity
    
    return res


# Example test
if __name__ == "__main__":
    appmem = [10, 6, 7, 12, 1]
    k = 3
    res = minimum_mem_cap(appmem, k)
    if res != -1:
        print(f"Minimum memory card capacity needed so every team can download at most 2 apps = {res}")
    else:
        print("Not possible")
"""

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