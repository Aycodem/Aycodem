try:
    x= int(input("Input an integer : "))
    print(x)
except:
    print("Something went wrong")
else:
    print("nothing went wrong")
finally:
    print("working")