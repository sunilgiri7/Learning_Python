while(True):
    print("press q to quite")
    a = input("enter a number:")
while(True):
    if a == 'q':
        break
    try:
        print("trying....")
        a = int(a)
        if a>6:
            print("you entered a number greater then 6")    
    except Execution as e:
        print(f"your input resulted in an error {e}")
        
print("thanks for playing this game") 