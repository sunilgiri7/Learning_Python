from logging import exception


try:
    a = int(input("enter a number"))
    c = 1/a
    print(c)
except exception as e:
    print("exception 1 occured")
    print(e)
    
except ZeroDivisionError as e:
    print("exception 2 occured")
    print(e)
print("thanks for using this code!")