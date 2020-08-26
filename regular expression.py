
import re
pattrn=r"color"
text="my fav color is black"

match=re.search(pattrn,text)
if match:
    print(match.start()) #eta pattern pawar por tar first letter er index print kore
    print(match.end())   #last letter er index print kore
    print(match.span())   #last & first letter duitar e index print kore
