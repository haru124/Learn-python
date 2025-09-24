def minimum_mem_cap(appmem, k):
    n = len(appmem)
    
    # If more apps than 2*k slots, not possible
    if n > 2 * k:
        return -1  
    
    appmem.sort()  # sort ascending
    
    def canDistribute(capacity):
        """Check if all apps can be assigned within k teams given capacity."""
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
