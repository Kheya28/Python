
import re
pattrn=r"[aeiou]"
#pattrn=r"[A-Z]" #A-Z jekono 1ta holei matched
#pattrn=r"[A-Z][a-z][0-9]"
if re.match(pattrn,"colour"): #pattern er jekono ekta match korlei matched
    print("matched")