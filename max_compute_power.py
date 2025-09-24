"""
Problem Statement

You are given two lists:

compute_powers[i] → the compute power of the i-th compute unit.
costs[i] → the cost of the i-th compute unit.

You are also given a budget.
You want to maximize the compute power you can purchase within your budget under these conditions:
You may purchase at most 2 compute units.
The total cost of selected units must not exceed the budget.
Return the maximum compute power achievable, along with the indices of the chosen units. If no unit can be bought within the budget, return 0.

EXAMPLE 1

Input:
compute_powers = [20, 50, 70, 90]
costs          = [5, 10, 15, 20]
budget = 25

Output:
Maximum Compute power we can afford within our budget with atmost 2 compute units :  120

Purchased Compute Units Details:    
Compute unit 2 : compute_power = 50, cost = 10
Compute unit 3 : compute_power = 70, cost = 15

EXAMPLE 2

Input:
compute_powers = [40, 30, 20]
costs          = [50, 60, 70]
budget = 40

Output:
We cant afford any compute units within our budget
"""

def max_compute(compute_powers
                ,costs,budget):
    n = len(compute_powers)
    maxCompPower = 0
    a,b = -1,-1
    minCost = min(costs)
    if minCost > budget:
        return maxCompPower,a,b
    for i in range(n):
        if costs[i] > budget:
            break
        else:
            if compute_powers[i] >= maxCompPower:
                maxCompPower = max(maxCompPower,compute_powers[i])
                a=i
                b = -1
                print("a in outer loop : ",a)
            for j in range(i+1,n):
                if costs[i] + costs[j] <= budget:
                    maxCompPower = max(maxCompPower,compute_powers[i]+compute_powers[j])
                    a = i
                    b = j
                    print(f"a: {a} b: {b}")
    return maxCompPower,a,b


if __name__=="__main__":
    compute_powers = list(map(int, input("Enter compute powers list: ").split()))
    costs = list(map(int, input("Enter cost of compute units list: ").split()))
    budget = int(input("Enter budget: "))
    
    max_compute_power,a,b = max_compute(compute_powers, costs, budget)
    
    if max_compute_power == 0:
        print("We cant afford any compute units within our budget")
    else:
        print("Maximum Compute power we can afford within our budget with atmost 2 compute units : ", max_compute_power)
        print(f"\nPurchased Compute Units Details: \nCompute unit {a+1} : compute_power = {compute_powers[a]}, cost = {costs[a]} \nCompute unit {b+1} : compute_power = {compute_powers[b]}, cost = {costs[b]}")
        
        
