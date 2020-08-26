
def fun(age):
    if age<18:
        raise ValueError("invalid voter")
    return  print("Valid voter")

try:
    fun(34)
    fun(11)
except ValueError as e:
    print(e)

