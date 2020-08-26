
import re
pattrn=r"color"
text="my fav color is black.This color is nice"

#match=re.sub(pattrn,"colour",text)
match=re.sub(pattrn,"colour",text,count=1) #ekhane count na dile text er je je jaygay pattern mile oi sobgula jaygay
#"colour" er moto hoye jabe r count bole dile shudhu first tototai replace korbe

print(match)