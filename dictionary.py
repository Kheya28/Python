
'''
stu_id={
    101:"rima",
    102:"nipa",
    103:"dipa"
}
'''


#key value can be integer or string
stu_id={
    "101":"rima",
    "102":"nipa",
    "103":"dipa"
}
print(stu_id.get("103"))
print(stu_id.get("104")) #as 104 is not valid,it will print none
print(stu_id.get("104","invalid key")) #we can also set a text


