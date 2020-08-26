
f=open("student.txt","r+")
#print(f.readable())
a=f.read()
print(a) # text file ta show korbe
size=len(a)
print(size)
f.close()

#text er line gulo jodi alada kore list e rakhte cai
f1=open("student.txt","r+")
lis=f1.readlines()
#lis1=lis=f1.readlines()[0]
print(lis)
#print(lis1)
f1.close()

#for loop use kore print kora
'''
for i in f:
    print(i)
'''

#https://www.youtube.com/watch?v=lnmonWbNIsQ