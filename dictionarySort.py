dic = {'a':40,'c':15,'f':20,'x':10,'l':25}

keys1 = sorted(dic, key = lambda x: dic[x])
print(keys1)

keys2 = sorted(dic.keys(), key = lambda x: dic[x])
print(keys2)

keys3 = [k for k, v in sorted(dic.items(), key=lambda item: item[1])]
print(keys3)

values1 = sorted(dic.values(), key = lambda x: x)
print(values1)

d2 = {v:k for k,v in dic.items()}

l1 = [23, 45, 12, 35, 27]

l2 = []
l = []
def swap(lst, index1, index2):
    lst[index1], lst[index2] = lst[index2], lst[index1]

for i in range(len(l1)):
    if l1[i] > 25:
        l2.append(i)
        l.append(l1[i])

print(f"l1: {l1}")
print(f"l2: {l2}")
print(f"l: {l}")
for i in range(len(l),0,-1):
    #print("i=",i)
    print(f"l[0:{i}] = {l[0:i]}")
    m = l.index(max(l[0:i]))
    print("argmax =",m)
    swap(l2,m,i-1)
    swap(l,m,i-1)
    
print(f"l2={l2}")