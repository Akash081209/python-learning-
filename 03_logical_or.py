while True:
    
    try:
        temperature = int(input("Enter your temperature:"))

        if temperature <10 or temperature > 45:
            print("Extreme temperature")
        else:
            print("Normal Temp")
    except:
        print("invalid please kindly enter an valid temperature")  