#set e value unordered thake
#index er sahajje value access kora jay na
#duplicate value rakha jay na

s={1,1,2,3,4}
print(s)

s1=set([4,5,6]) # set evabeo create kora jay
s1.add(7)
s1.remove(4)
print(s1)

print(7 in s1) # s1 e 7 ache kina check kora
print(7 not in s1)

print(s|s1)  #union(sob newa)
print(s&s1)  #intersection(common value newa)
print(s-s1)  #s1 set minus kora

