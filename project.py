print("===== BEAN & BREW =====")
print("1. Expresso - 120")
print("2. Latte - ₹180")
print("3. Cappuccino - ₹180")
print("4. Mocha - ₹210")
print("5 .cold coffee - 170")


name = input("Enter your name :")
coffee = input("Enter your coffee:")
quantity = int(input("Enter how much coffee you want:"))

if coffee=="Espresso":
    price = 120

elif coffee == "Latte":
    price = 180

elif coffee == "cappuccino":
    price = 180

elif coffee == "Mocha": 
    price = 210


Total = price * quantity
print(Total)


print("=======Order bill========")
print("Customer name:", name)
print("You ordered:", coffee)
print("your quantity:", quantity)
print("Your total bill is:", Total)
print("Thank you!")
print("Visit again!") 
















