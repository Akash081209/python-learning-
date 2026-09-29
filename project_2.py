while True:
    name=input("Enter your name:")
    math=int(input("Enter your math marks:"))
    science=int(input("Enter your science marks:"))
    python=int(input("Enter your python marks:"))
    Total = math + science + python
    Average = Total / 3 

    if Total>=200:
        grade = "A+"
    elif Total>=180:
        grade = "A"
    elif Total < 180:
        grade = "B"

    if Total >=80:
        result = "passed"
    elif Total<80:
        result="failed"
        
    print("====RESULT====")
    print("Math:",math)
    print("Science:", science)
    print("Python:",python)
    print("Total:", Total)
    print("Average", Average)
    print("Result:",result)
    print("Grade", grade)
    Next = input("Do you want to analyze another student result:")
    if Next == "NO":
        break
    elif Next == "Yes":
        print("YOU can check again")
    else:
        print("Please enter an valid answer")



        


