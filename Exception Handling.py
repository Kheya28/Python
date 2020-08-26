
try:
    list=[10,20,0]
    p=list[0]/list[2] #it causes dividing by zero
    print(p)
    p=list[2]/list[4] #it causes index error


except ZeroDivisionError:
    print("dividing by zero isn't possible")
except IndexError:
    print("poor size")
except ValueError:  # int input newar somoy kew jodi float ney
    print("enter the correct data type")
except (ZeroDivisionError,IndexError,ValueError):  # sob exception eksathe dite caile
    print("incorrect data")
finally:  # je exception e hok na keno etar vitor sob must kaj korbe
    print("must print")

