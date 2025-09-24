house = [1,2,3,1]

n = len(house)


dp = [0]*(n+1)
m =0

for i in range(n):
    dp[i+1] = max(house[i], dp[i-1]+house[i]) 
    m = max(m,dp[i+1])
    
print(dp)
print("max profit if only non adjacent houses can be robbed is ", m)