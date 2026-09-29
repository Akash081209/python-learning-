while True:
    Totalsubjects = ("maths","science","engineering","cosmology","english")
    
    name = input("Enter your name :")
    maths = int(input("Enter your math marks:"))
    science = int(input("Enter your science marks:"))
    cosmology = int(input("Enter your cosmology:"))
    english = int(input("Enter your english marks:"))
    engineering = int(input("Enter your engineering marks:"))
    
    Total = maths + science + cosmology + english + engineering
    
    totallysubjects = (len(Totalsubjects))
    mostmarksubject = (max(maths,science,engineering,cosmology,english))
    lessmarksubject = (min(maths,science,engineering,cosmology,english))
    average = Total / 5

    if Total >=490:
        grade = "A+"

    elif Total >=375:
        grade = "A"

    elif Total >=260:
        grade = "B"

    elif Total >=140:
        grade = "C"

    else:
        grade = "F"
    print("==== RESULT====")
    print("Student name :",name)
    print("Marks", maths , science , engineering, english , cosmology)
    print("Total is :",Total)
    print("Total subjects are :",totallysubjects)
    print("Your average is :",average)
    print("Highest:", mostmarksubject)
    print("lowest:", lessmarksubject)
    print("Your grade is :",grade)
    doyouwant = input("do you want to see another student result:")
    if doyouwant == "No":
        break
    elif doyouwant == "Yes":
        print("Check again")