#LIFO
from collections import deque

st=[]
st.append("aaa")
st.append("bbb")
st.append("ccc")
st.pop()
print(st)
print(st[-1])
st.pop()
st.pop()
if not st:
    print("no elements in stack")

#queue
q=deque(["aa","bb"])
q.popleft()

print(q)

if not q:
    print("empty")
else: print("not empty")