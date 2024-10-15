# simple match case statement
def runMatch():
    num = int(input("Enter a number between 1 and 3: "))
    
    # match case
    match num:
        # pattern 1
        case 1 | 4 | 5:
            print("One")
        # pattern 2
        case (2 or 6):
            print("Two")
        # pattern 3
        case 3:
            print("Three")
        # default pattern
        case _:
            print("Number not between 1 and 3")
            
runMatch()